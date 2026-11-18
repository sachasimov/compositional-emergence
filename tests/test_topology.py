import numpy as np
import pytest

from compositional_emergence.automata import life_step
from compositional_emergence.benchmark_localized import obj, trajectory, match_objects, prediction, TOAD, TOAD_PHASE, BLOCK
from compositional_emergence.benchmark_topology import fixtures, GLIDER_PHASES, TUB
from compositional_emergence.localized import detect_candidates
from compositional_emergence.localized_v2 import detect_candidates_v2, spacetime_groups


def accepted(result):
    return [prediction(t["initial_live_cells"], t["recurrence"])
            for t in result["tracks"] if t["status"] == "candidate"]


@pytest.mark.parametrize("phase", [TOAD, TOAD_PHASE])
def test_temporal_union_recovers_both_toad_phases_while_identical_edge_ablation_misses(phase):
    truth = [obj("toad", phase, (20, 20), 2)]
    data = trajectory(truth[0]["initial_live_cells"], 12)
    result = detect_candidates_v2(data)
    assert match_objects(accepted(result), truth)["tp"] == 1
    assert result["tracks"][0]["multipart_at_some_frame"]
    ablated = detect_candidates_v2(data, association="one-to-one-overlap")
    assert not accepted(ablated)
    assert any(t["reason"] == "no-window-start-support" for t in ablated["tracks"])


def test_nearby_blocks_are_separate_without_radius_two_or_dictionary_exceptions():
    truth = [obj("a", BLOCK, (16, 16), 1), obj("b", BLOCK, (16, 19), 1)]
    data = trajectory([p for o in truth for p in o["initial_live_cells"]], 12)
    assert detect_candidates(data)["candidate_count"] == 0
    for association in ("overlap-union", "one-to-one-overlap"):
        result = detect_candidates_v2(data, association=association)
        assert match_objects(accepted(result), truth)["tp"] == 2
        assert result["graph"]["observed_overlap_edges"] == result["graph"]["selected_overlap_edges"]


def scalar_step(a):
    result = np.zeros_like(a)
    h, w = a.shape
    for y in range(h):
        for x in range(w):
            count = sum(int(a[(y+dy) % h, (x+dx) % w]) for dy in (-1, 0, 1)
                        for dx in (-1, 0, 1) if dy or dx)
            result[y, x] = count == 3 or (a[y, x] and count == 2)
    return result


def test_independent_stationary_tub_decomposition_exposes_geometric_false_fusion():
    truth = [obj("a", TUB, (20, 20), 1), obj("b", TUB, (22, 22), 1)]
    for o in truth:
        initial = trajectory(o["initial_live_cells"], 0)[0]
        assert np.array_equal(scalar_step(initial), initial)
    data = trajectory([p for o in truth for p in o["initial_live_cells"]], 12)
    assert np.array_equal(scalar_step(data[0]), data[0])
    result = detect_candidates_v2(data)
    score = match_objects(accepted(result), truth)
    # The supplied two-part decomposition is deliberately not uniquely geometric.
    assert (score["tp"], score["fp"], score["fn"]) == (0, 1, 2)


def test_prospective_stationary_block_constructions_are_independently_stationary():
    selected = [c for c in fixtures() if c["split"] == "prospective-fixed" and
                "block" in c["id"]]
    assert len(selected) == 5
    for case in selected:
        a = trajectory(case["initial_live_cells"], 0)[0]
        assert np.array_equal(scalar_step(a), a)


def test_explicit_glider_phases_follow_independent_reference_and_shifted_return():
    states = [trajectory(obj("g", points, (12, 12), 4, (1, 1))["initial_live_cells"], 0)[0]
              for points in GLIDER_PHASES]
    for phase in range(4):
        expected = states[phase+1] if phase < 3 else np.roll(states[0], (1, 1), axis=(0, 1))
        assert np.array_equal(scalar_step(states[phase]), expected)


def test_groups_born_after_window_start_are_explicitly_excluded():
    data = trajectory([(20, 20), (20, 22), (22, 20)], 12)
    assert np.argwhere(data[1]).tolist() == [[21, 21]]
    assert not data[2].any()
    result = detect_candidates_v2(data)
    born = [t for t in result["tracks"] if t["first_observed_frame"] > 0]
    assert len(born) == 1
    assert born[0]["initial_live_cells"] == []
    assert born[0]["reason"] == "no-window-start-support"
    assert not accepted(result)


def test_graph_groups_partition_every_observed_cell_without_duplicate_hypotheses():
    data = trajectory(obj("toad", TOAD_PHASE, (20, 20), 2)["initial_live_cells"], 12)
    for association in ("overlap-union", "one-to-one-overlap"):
        nodes, groups, _ = spacetime_groups(data, association)
        assigned = [i for group in groups for i in group]
        assert sorted(assigned) == list(range(len(nodes)))
        for t in range(len(data)):
            seen = set()
            for group in groups:
                points = {p for i in group if nodes[i][0] == t for p in nodes[i][1]}
                assert not seen & points
                seen.update(points)
            assert seen == {tuple(p) for p in np.argwhere(data[t])}


def test_disjoint_coordinate_frames_do_not_receive_invented_temporal_links():
    # Graph-unit fixture only, not claimed to be a Life trajectory or object.
    data = np.zeros((2, 8, 8), dtype=np.uint8)
    data[0, 2, 2] = 1
    data[1, 4, 4] = 1
    _, groups, graph = spacetime_groups(data)
    assert len(groups) == 2 and graph["observed_overlap_edges"] == 0


def test_invalid_data_modes_and_short_observations_are_rejected_or_abstained():
    data = trajectory(obj("toad", TOAD_PHASE, (20, 20), 2)["initial_live_cells"], 2)
    result = detect_candidates_v2(data)
    assert result["tracks"][0]["reason"] == "insufficient-observed-cycles"
    with pytest.raises(ValueError, match="association"):
        detect_candidates_v2(data, association="unknown")
    corrupt = data.copy()
    corrupt[1, 40, 40] = 1
    with pytest.raises(ValueError, match="violates Life"):
        detect_candidates_v2(corrupt)
    with pytest.raises(ValueError):
        detect_candidates_v2(data, min_cycles=1)


def test_fixed_panel_counts_and_regression_provenance():
    panel = fixtures()
    assert len(panel) == len({c["id"] for c in panel}) == 38
    assert sum(c["scored"] for c in panel) == 29
    assert sum(len(c["truth_objects"]) for c in panel if c["scored"]) == 38
    assert sum(c["split"] == "development-regression" for c in panel) == 14
    assert sum(c["split"] == "prospective-fixed" for c in panel) == 15
    assert sum(c["split"] == "diagnostic" for c in panel) == 9
    assert all(c["split"] != "held-out" for c in panel)


def test_topology_benchmark_never_overwrites_prior_evidence(tmp_path, monkeypatch):
    from compositional_emergence import benchmark_topology
    output = tmp_path / "evidence.json"
    output.write_bytes(b"preserved")
    monkeypatch.setattr(benchmark_topology, "run", lambda _: pytest.fail("must not execute"))
    with pytest.raises(SystemExit):
        benchmark_topology.main(["--output", str(output)])
    assert output.read_bytes() == b"preserved"
