"""Prespecified cycle-002 engineered localized-candidate validation panel."""
import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from .automata import life_step
from .localized import detect_candidates
from .provenance import source_provenance, state_hash
from .structures import exact_translational_recurrence


# Ground-truth fixtures are analytic supplied supports, never detector outputs.
BLOCK = [(0, 0), (0, 1), (1, 0), (1, 1)]
BLINKER = [(0, 0), (0, 1), (0, 2)]
GLIDER = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
TOAD = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2)]
TOAD_PHASE = [(-1, 2), (0, 0), (0, 3), (1, 0), (1, 3), (2, 1)]


def obj(name, points, offset, period, displacement=(0, 0)):
    return {"name": name,
            "initial_live_cells": sorted([[(y+offset[0]) % 48, (x+offset[1]) % 48]
                                           for y, x in points]),
            "period": period, "displacement": list(displacement)}


def fixtures():
    panel = []
    def add(name, objects, split="development", extra=(), steps=12,
            scored=True, regime="validated-isolation", **metadata):
        cells = {tuple(p) for o in objects for p in o["initial_live_cells"]}
        cells.update(tuple(p) for p in extra)
        panel.append({"id": name, "split": split, "scored": scored,
                      "regime": regime, "steps": steps,
                      "initial_live_cells": [list(p) for p in sorted(cells)],
                      "truth_objects": objects, **metadata})
    b = lambda offset: obj("block", BLOCK, offset, 1)
    g = lambda offset: obj("glider-SE", GLIDER, offset, 4, (1, 1))
    add("block", [b((12, 12))])
    add("blinker", [obj("blinker", BLINKER, (12, 12), 2)])
    add("glider", [g((12, 12))])
    add("toad", [obj("toad", TOAD, (12, 12), 2)])
    add("stationary-plus-moving", [b((8, 8)), g((26, 26))])
    add("two-different-velocities", [g((25, 25)),
        obj("glider-NW", [(2-y, 2-x) for y, x in GLIDER], (10, 10), 4, (-1, -1))])
    add("empty", [])
    add("single-transient", [], extra=[(12, 12)])
    add("pair-transient", [], extra=[(12, 12), (12, 13)])
    add("reflected-translated-glider", [obj("glider-SW", [(y, -x) for y, x in GLIDER],
                                           (24, 24), 4, (1, -1))], "held-out")
    add("rotated-translated-toad", [obj("rotated-toad", [(x, -y) for y, x in TOAD],
                                      (24, 24), 2)], "held-out")
    add("three-separated", [b((8, 8)), obj("blinker", BLINKER, (8, 32), 2),
        obj("glider-SW", [(y, -x) for y, x in GLIDER], (30, 32), 4, (1, -1))], "held-out")
    add("nearby-independent-blocks", [b((14, 14)), b((14, 17))], "held-out",
        regime="known-segmentation-limit",
        annotation="Two known stationary blocks separated by one empty column; radius-two grouping may fuse them.")
    add("phase-shifted-toad", [obj("toad-other-phase", TOAD_PHASE, (24, 24), 2)],
        "held-out", regime="known-segmentation-limit",
        annotation="Known period-two oscillator with disconnected initial eight-neighbor support.")
    add("short-window-blinker", [obj("blinker", BLINKER, (12, 12), 2)],
        "diagnostic", steps=2, scored=False, regime="insufficient-window",
        annotation="Known oscillator but fewer than two observed periods; must abstain.")
    add("periodic-edge-glider", [g((46, 46))], "diagnostic", scored=False,
        regime="boundary", annotation="Known periodic spaceship crosses edge; method must abstain rather than unwrap.")
    overlap = set(map(tuple, obj("a", BLOCK, (18, 18), 1)["initial_live_cells"]))
    overlap.update(map(tuple, obj("b", BLOCK, (19, 19), 1)["initial_live_cells"]))
    add("overlapping-engineered-blocks", [], "diagnostic", extra=overlap,
        scored=False, regime="unlabelled-overlap",
        annotation="Overlapping supports lack independent object annotations; no product-identity inference.")
    collision = g((18, 18))["initial_live_cells"] + obj("opposed", [(2-y, 2-x) for y, x in GLIDER],
                                                        (25, 25), 4, (-1, -1))["initial_live_cells"]
    add("opposed-glider-encounter", [], "diagnostic", extra=collision, scored=False,
        regime="interaction", annotation="Engineered approach/encounter; no collision-product ground truth. Must not emit a complete isolated track.")
    for seed in (13, 17):
        rng = np.random.Generator(np.random.PCG64(seed))
        cells = np.argwhere(rng.random((48, 48)) < 0.12).tolist()
        add(f"clutter-seed-{seed}", [], "diagnostic", extra=cells, scored=False,
            regime="unlabelled-clutter", seed=seed, rng="PCG64", density=0.12,
            annotation="Fixed engineered challenge; unlabelled does not mean object-free.")
    return panel


def trajectory(cells, steps):
    state = np.zeros((48, 48), dtype=np.uint8)
    if cells:
        ys, xs = zip(*cells)
        state[ys, xs] = 1
    data = [state]
    for _ in range(steps):
        data.append(life_step(data[-1]))
    return np.stack(data)


def signature(o):
    return (tuple(sorted(tuple(p) for p in o["initial_live_cells"])),
            o["period"], tuple(o["displacement"]))


def match_objects(predictions, truth):
    """Exact footprint plus period/displacement; a prediction matches at most once."""
    remaining = list(range(len(truth)))
    matches, unmatched_predictions = [], []
    for i, predicted in enumerate(predictions):
        match = next((j for j in remaining if signature(predicted) == signature(truth[j])), None)
        if match is None:
            unmatched_predictions.append(i)
        else:
            matches.append({"prediction": i, "truth": match})
            remaining.remove(match)
    return {"tp": len(matches), "fp": len(unmatched_predictions), "fn": len(remaining),
            "matches": matches, "unmatched_predictions": unmatched_predictions,
            "unmatched_truth": remaining, "predicted_count": len(predictions),
            "truth_count": len(truth), "absolute_count_error": abs(len(predictions)-len(truth))}


def prediction(cells, recurrence):
    return {"initial_live_cells": cells, "period": recurrence["period"],
            "displacement": list(recurrence["displacement"])}


def summarize(rows, method):
    selected = [r for r in rows if r["scored"]]
    good = [r for r in selected if r["status"] == "ok"]
    totals = {k: sum(r["evaluation"][method][k] for r in good) for k in ("tp", "fp", "fn")}
    tp, fp, fn = (totals[k] for k in ("tp", "fp", "fn"))
    negative = [r for r in good if not r["truth_objects"]]
    ratio = lambda n, d: n/d if d else None
    return {**totals, "n_scored_cases": len(selected), "n_case_errors": len(selected)-len(good),
            "precision": ratio(tp, tp+fp), "recall": ratio(tp, tp+fn),
            "count_mae": ratio(sum(r["evaluation"][method]["absolute_count_error"] for r in good), len(good)),
            "negative_cases_with_false_prediction": sum(r["evaluation"][method]["fp"] > 0 for r in negative),
            "n_negative_cases": len(negative)}


def run(protocol):
    started = time.perf_counter()
    output = {"experiment_id": "CE-001", "cycle": "002", "protocol_version": "localized-v1",
              "evidence_state": "engineered-method-validation-not-physical-object-identification",
              "protocol_sha256": hashlib.sha256(protocol.read_bytes()).hexdigest(),
              "provenance": source_provenance(), "rule": "B3/S23", "boundary": "periodic",
              "shape": [48, 48], "hash_encoding": "C-order uint8 bytes", "cases": []}
    for case in fixtures():
        row = dict(case)
        try:
            data = trajectory(case["initial_live_cells"], case["steps"])
            row["trajectory_sha256_by_frame"] = [state_hash(frame) for frame in data]
            detection = detect_candidates(data)
            candidates = [prediction(t["initial_live_cells"], t["recurrence"])
                          for t in detection["tracks"] if t["status"] == "candidate"]
            whole = exact_translational_recurrence(data[0], max_period=4, max_shift=2)
            if whole is not None and 2 * whole.period > case["steps"]:
                whole = None  # Same two-observed-cycle requirement as localized candidates.
            predictions = {"localized": candidates,
                           "whole_grid": [prediction(case["initial_live_cells"], asdict(whole))] if whole else [],
                           "occupancy_static": [prediction(case["initial_live_cells"],
                                                  {"period": 1, "displacement": [0, 0]})]
                           if case["initial_live_cells"] else []}
            row.update(status="ok", detection=detection, predictions=predictions,
                       evaluation={method: match_objects(pred, case["truth_objects"])
                                   for method, pred in predictions.items()} if case["scored"] else None)
            # Diagnostics remain unscored, including any unexpected candidates.
        except Exception as exc:
            row.update(status="error", error=f"{type(exc).__name__}: {exc}")
        output["cases"].append(row)
    output["metrics"] = {split: {method: summarize(
        [r for r in output["cases"] if split == "combined" or r["split"] == split], method)
        for method in ("localized", "whole_grid", "occupancy_static")}
        for split in ("development", "held-out", "combined")}
    safe = [r for r in output["cases"] if r["scored"] and r["regime"] == "validated-isolation"]
    mandatory_abstain = [r for r in output["cases"] if r["regime"] in
                        ("insufficient-window", "boundary", "interaction")]
    moving = [r for r in output["cases"] if r["id"] in
              ("stationary-plus-moving", "two-different-velocities")]
    output["expectations"] = {
        "all_cases_without_exceptions": all(r["status"] == "ok" for r in output["cases"]),
        "isolated_fixtures_exactly_matched": all(r["status"] == "ok" and
            r["evaluation"]["localized"]["fp"] == r["evaluation"]["localized"]["fn"] == 0 for r in safe),
        "required_out_of_regime_abstentions": all(r["status"] == "ok" and
            not r["predictions"]["localized"] for r in mandatory_abstain),
        "different_velocities_improve_over_whole_grid": all(r["status"] == "ok" and
            r["evaluation"]["localized"]["tp"] > r["evaluation"]["whole_grid"]["tp"]
            for r in moving)}
    output["elapsed_seconds"] = time.perf_counter()-started
    output["passed_prespecified_expectations"] = all(output["expectations"].values())
    return output


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--protocol", type=Path,
                        default=Path(__file__).resolve().parents[2] / "experiments/CE-001/cycle-002-localized-v1.md")
    args = parser.parse_args(argv)
    if args.output.exists():
        parser.error("output already exists; preserve previous evidence")
    result = run(args.protocol)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with args.output.open("x", encoding="utf-8") as stream:
            stream.write(json.dumps(result, indent=2) + "\n")
    except FileExistsError:
        parser.error("output already exists; preserve previous evidence")
    if not result["passed_prespecified_expectations"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
