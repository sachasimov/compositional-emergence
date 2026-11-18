"""Cycle-003 fixed engineered topology/phase sensitivity benchmark."""
import argparse
import hashlib
import json
from pathlib import Path
import time

from .benchmark_localized import (
    fixtures as previous_fixtures, obj, trajectory, prediction, match_objects,
    summarize, BLOCK, BLINKER, GLIDER, TOAD, TOAD_PHASE)
from .localized import detect_candidates
from .localized_v2 import detect_candidates_v2
from .provenance import source_provenance, state_hash


# Explicit analytic phases, supplied before running either detector.
GLIDER_PHASES = [GLIDER,
    [(1, 0), (1, 2), (2, 1), (2, 2), (3, 1)],
    [(1, 2), (2, 0), (2, 2), (3, 1), (3, 2)],
    [(1, 1), (2, 2), (2, 3), (3, 1), (3, 2)]]
TUB = [(0, 1), (1, 0), (1, 2), (2, 1)]


def fixtures():
    panel = []
    for old in previous_fixtures():
        row = dict(old)
        row["cycle002_original_split"] = row["split"]
        row["split"] = "development-regression" if row["scored"] else "diagnostic"
        row["origin"] = "cycle002-known-development-regression" if row["scored"] else "cycle002-known-diagnostic"
        panel.append(row)
    def add(name, objects, extra=(), scored=True, steps=12,
            regime="prospective-isolated", **metadata):
        cells = {tuple(p) for o in objects for p in o["initial_live_cells"]}
        cells.update(tuple(p) for p in extra)
        panel.append({"id": name, "split": "prospective-fixed" if scored else "diagnostic",
                      "origin": "cycle003-prospective-fixed", "scored": scored,
                      "regime": regime, "steps": steps,
                      "initial_live_cells": [list(p) for p in sorted(cells)],
                      "truth_objects": objects, **metadata})
    for phase, points in enumerate(GLIDER_PHASES):
        add(f"prospective-glider-phase-{phase}",
            [obj(f"glider-phase-{phase}", points, (14+phase*2, 20), 4, (1, 1))])
    for phase, points in enumerate((TOAD, TOAD_PHASE)):
        add(f"prospective-rotated-toad-phase-{phase}",
            [obj(f"toad-phase-{phase}", [(x, -y) for y, x in points], (12, 32), 2)])
    add("prospective-vertical-blinker", [obj("vertical-blinker", [(x, y) for y, x in BLINKER],
                                            (28, 28), 2)])
    for delta in (3, 4, 6):
        add(f"prospective-block-spacing-{delta}",
            [obj("left-block", BLOCK, (16, 16), 1),
             obj("right-block", BLOCK, (16, 16+delta), 1)])
    add("prospective-vertical-near-blocks", [obj("top-block", BLOCK, (16, 16), 1),
                                            obj("bottom-block", BLOCK, (19, 16), 1)])
    add("prospective-diagonal-near-blocks", [obj("NW-block", BLOCK, (16, 16), 1),
                                            obj("SE-block", BLOCK, (19, 19), 1)])
    add("prospective-single-tub", [obj("tub", TUB, (20, 20), 1)])
    add("prospective-diagonal-tubs-decomposition", [obj("NW-tub", TUB, (20, 20), 1),
                                                   obj("SE-tub", TUB, (22, 22), 1)],
        regime="prospective-decomposition-ambiguity",
        annotation="Each supplied tub and their union are independently stationary. Eight-connectivity merges them; supplied two-object truth is a conventional decomposition, not unique physical identity. Keep FP/FNs if a composite is emitted.")
    add("prospective-multipart-plus-moving", [obj("toad-other-phase", TOAD_PHASE, (10, 10), 2),
        obj("glider-other-phase", GLIDER_PHASES[1], (28, 28), 4, (1, 1))])
    add("prospective-short-multipart-toad", [obj("toad-other-phase", TOAD_PHASE, (20, 20), 2)],
        scored=False, steps=2, regime="insufficient-window",
        annotation="Known multipart oscillator, fewer than two observed periods; no candidate.")
    add("prospective-boundary-multipart-toad", [obj("toad-other-phase", TOAD_PHASE, (1, 1), 2)],
        scored=False, regime="boundary", annotation="Boundary ambiguity; no unwrapping.")
    add("prospective-born-transient", [], extra=[(20, 20), (20, 22), (22, 20)],
        scored=False, regime="born-after-window-start",
        annotation="Three separated parents die; center (21,21) is born then dies. A graph group with no t=0 support must be explicitly excluded; no object-identity truth supplied.")
    return panel


def run(protocol):
    started = time.perf_counter()
    output = {"experiment_id": "CE-001", "cycle": "003", "protocol_version": "topology-v1",
              "evidence_state": "engineered-topological-candidate-validation-not-object-individuation",
              "protocol_sha256": hashlib.sha256(protocol.read_bytes()).hexdigest(),
              "provenance": source_provenance(), "rule": "B3/S23", "boundary": "periodic",
              "shape": [48, 48], "hash_encoding": "C-order uint8 bytes", "cases": []}
    for case in fixtures():
        row = dict(case)
        try:
            data = trajectory(case["initial_live_cells"], case["steps"])
            detections = {"topological_v2": detect_candidates_v2(data),
                          "localized_v1": detect_candidates(data),
                          "one_to_one_ablation": detect_candidates_v2(data, association="one-to-one-overlap")}
            predictions = {method: [prediction(t["initial_live_cells"], t["recurrence"])
                                   for t in detected["tracks"] if t["status"] == "candidate"]
                           for method, detected in detections.items()}
            row.update(status="ok", trajectory_sha256_by_frame=[state_hash(frame) for frame in data],
                       detections=detections, predictions=predictions,
                       evaluation={method: match_objects(pred, case["truth_objects"])
                                   for method, pred in predictions.items()} if case["scored"] else None)
        except Exception as exc:
            row.update(status="error", error=f"{type(exc).__name__}: {exc}")
        output["cases"].append(row)
    methods = ("topological_v2", "localized_v1", "one_to_one_ablation")
    output["metrics"] = {split: {method: summarize(
        [r for r in output["cases"] if split == "combined" or r["split"] == split], method)
        for method in methods} for split in ("development-regression", "prospective-fixed", "combined")}
    repaired = [r for r in output["cases"] if r["id"] in ("nearby-independent-blocks", "phase-shifted-toad")]
    safe = [r for r in output["cases"] if r["scored"] and
            r["regime"] != "prospective-decomposition-ambiguity"]
    abstentions = [r for r in output["cases"] if r["regime"] in
                   ("insufficient-window", "boundary", "interaction")]
    output["expectations"] = {
        "all_cases_without_exceptions": all(r["status"] == "ok" for r in output["cases"]),
        "previous_three_misses_recovered": all(r["status"] == "ok" and
            r["evaluation"]["topological_v2"]["fp"] == r["evaluation"]["topological_v2"]["fn"] == 0
            for r in repaired),
        "declared_isolated_cases_exactly_matched": all(r["status"] == "ok" and
            r["evaluation"]["topological_v2"]["fp"] == r["evaluation"]["topological_v2"]["fn"] == 0
            for r in safe),
        "required_out_of_regime_abstentions": all(r["status"] == "ok" and
            not r["predictions"]["topological_v2"] for r in abstentions)}
    output["elapsed_seconds"] = time.perf_counter()-started
    output["passed_prespecified_expectations"] = all(output["expectations"].values())
    return output


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--protocol", type=Path,
                        default=Path(__file__).resolve().parents[2] / "experiments/CE-001/cycle-003-topology-v1.md")
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
