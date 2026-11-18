import numpy as np
import pytest

from compositional_emergence.automata import life_step
from compositional_emergence.benchmark_localized import (
    fixtures, match_objects, obj, trajectory, BLOCK, BLINKER, GLIDER, TOAD, TOAD_PHASE)
from compositional_emergence.localized import components, detect_candidates


def test_recovers_separated_static_and_moving_supports_without_global_translation():
    truth = [obj("block", BLOCK, (8, 8), 1), obj("glider", GLIDER, (26, 26), 4, (1, 1))]
    cells = [p for o in truth for p in o["initial_live_cells"]]
    result = detect_candidates(trajectory(cells, 12))
    predictions = [{"initial_live_cells": t["initial_live_cells"], **t["recurrence"]}
                   for t in result["tracks"] if t["status"] == "candidate"]
    score = match_objects(predictions, truth)
    assert (score["tp"], score["fp"], score["fn"]) == (2, 0, 0)
    assert all(len(t["support_sha256_by_frame"]) == 13 for t in result["tracks"])


@pytest.mark.parametrize("points,period,shift", [(BLOCK, 1, (0, 0)), (BLINKER, 2, (0, 0)),
                                                 (GLIDER, 4, (1, 1)), (TOAD, 2, (0, 0)),
                                                 (TOAD_PHASE, 2, (0, 0))])
def test_analytic_truth_cycles_are_verified_without_detector_labels(points, period, shift):
    cells = obj("known", points, (20, 20), period, shift)["initial_live_cells"]
    data = trajectory(cells, 2*period)
    assert np.array_equal(data[period], np.roll(data[0], shift, axis=(0, 1)))
    assert np.array_equal(data[2*period], np.roll(data[0], tuple(2*x for x in shift), axis=(0, 1)))
    if period > 1:
        assert not np.array_equal(data[1], data[0])


def test_nearby_blocks_stay_independently_stationary_but_conservative_grouping_misses_them():
    objects = [obj("a", BLOCK, (14, 14), 1), obj("b", BLOCK, (14, 17), 1)]
    cells = [p for o in objects for p in o["initial_live_cells"]]
    data = trajectory(cells, 12)
    assert all(np.array_equal(frame, data[0]) for frame in data)
    assert len(components(data[0], radius=1)) == 2
    assert len(components(data[0], radius=2)) == 1
    result = detect_candidates(data)
    assert result["candidate_count"] == 0
    assert result["tracks"][0]["reason"] == "initial-segmentation-ambiguity"
    assert match_objects([], objects)["fn"] == 2


def test_phase_shifted_toad_is_an_explicit_false_negative():
    cells = obj("phase", TOAD_PHASE, (20, 20), 2)["initial_live_cells"]
    result = detect_candidates(trajectory(cells, 12))
    assert result["candidate_count"] == 0
    assert result["tracks"][0]["reason"] == "initial-segmentation-ambiguity"


def test_matching_rejects_duplicates_wrong_footprints_and_wrong_signatures():
    truth = [obj("block", BLOCK, (12, 12), 1)]
    wrong_period = {**truth[0], "period": 2}
    wrong_shift = {**truth[0], "displacement": [1, 0]}
    wrong_support = {**truth[0], "initial_live_cells": truth[0]["initial_live_cells"][:-1]}
    for prediction in (wrong_period, wrong_shift, wrong_support):
        result = match_objects([prediction], truth)
        assert (result["tp"], result["fp"], result["fn"]) == (0, 1, 1)
    result = match_objects([truth[0], truth[0]], truth)
    assert (result["tp"], result["fp"], result["fn"]) == (1, 1, 0)


def test_temporally_inconsistent_data_and_invalid_limits_are_rejected():
    data = trajectory(obj("block", BLOCK, (12, 12), 1)["initial_live_cells"], 3)
    corrupt = data.copy()
    corrupt[1, 30, 30] = 1
    with pytest.raises(ValueError, match="violates Life"):
        detect_candidates(corrupt)
    for kwargs in [{"min_cycles": 1}, {"max_period": 1.5}, {"edge_margin": 0}, {"max_shift": -1}]:
        with pytest.raises(ValueError):
            detect_candidates(data, **kwargs)


def test_insufficient_cycles_and_edge_proximity_abstain():
    short = trajectory(obj("blinker", BLINKER, (12, 12), 2)["initial_live_cells"], 2)
    assert detect_candidates(short)["tracks"][0]["reason"] == "insufficient-observed-cycles"
    edge = trajectory(obj("block", BLOCK, (1, 1), 1)["initial_live_cells"], 12)
    assert detect_candidates(edge)["tracks"][0]["reason"] == "boundary-proximity"


def test_fixed_panel_labels_and_split_counts():
    panel = fixtures()
    assert len(panel) == 20
    assert len({c["id"] for c in panel}) == 20
    assert sum(c["scored"] for c in panel) == 14
    assert sum(len(c["truth_objects"]) for c in panel if c["scored"]) == 16
    assert all(not c["scored"] for c in panel if c["split"] == "diagnostic")


def test_benchmark_preserves_existing_evidence_without_running(tmp_path, monkeypatch):
    from compositional_emergence import benchmark_localized
    output = tmp_path / "evidence.json"
    output.write_bytes(b"original evidence")
    monkeypatch.setattr(benchmark_localized, "run", lambda path: pytest.fail("must not execute"))
    with pytest.raises(SystemExit):
        benchmark_localized.main(["--output", str(output)])
    assert output.read_bytes() == b"original evidence"
