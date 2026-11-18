"""Fixed CE-001 assay validation pilot; no spontaneous discovery or object tracking."""
import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from .automata import life_step
from .provenance import source_provenance, state_hash
from .structures import exact_translational_recurrence


BLOCK = [(0, 0), (0, 1), (1, 0), (1, 1)]
BLINKER = [(0, 0), (0, 1), (0, 2)]
GLIDER = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
TOAD = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2)]


def grid(points, offset=(10, 10), size=32):
    state = np.zeros((size, size), dtype=np.uint8)
    for y, x in points:
        state[(y + offset[0]) % size, (x + offset[1]) % size] = 1
    return state


def cases():
    """A priori labels: analytic fixtures only; diagnostics are deliberately unscored."""
    panel = []
    def add(name, points, label, split="development", **kwargs):
        panel.append({"id": name, "initial": grid(points), "label": label,
                      "split": split, "max_period": 12, "max_shift": 4, **kwargs})
    for name, points in [("block", BLOCK), ("blinker", BLINKER),
                         ("glider", GLIDER), ("toad", TOAD)]:
        add(name, points, True)
    for name, points in [("empty", []), ("single", [(0, 0)]),
                         ("adjacent-pair", [(0, 0), (0, 1)]),
                         ("separated-pair", [(0, 0), (5, 5)])]:
        add(name, points, False)
    add("reflected-glider", [(y, -x) for y, x in GLIDER], True, "held-out")
    add("rotated-toad", [(x, -y) for y, x in TOAD], True, "held-out")
    add("diagonal-pair", [(0, 0), (1, 1)], False, "held-out")
    add("short-window-blinker", BLINKER, None, "diagnostic", max_period=1,
        limitation="Known oscillator is missed when the period window is too short.")
    add("zero-shift-glider", GLIDER, None, "diagnostic", max_period=4, max_shift=0,
        limitation="Known spaceship is missed without translational matching.")
    add("mixed-block-glider", BLOCK + [(y+10, x+10) for y, x in GLIDER], None,
        "diagnostic", limitation="One global translation cannot represent independently moving objects.")
    add("edge-glider", GLIDER, None, "diagnostic", initial=grid(GLIDER, (30, 30)),
        limitation="Periodic recurrence can hold across wraparound; no free-space identity inference.")
    add("overlapping-blocks", BLOCK + [(y+1, x+1) for y, x in BLOCK], None,
        "diagnostic", limitation="Overlapping engineered patterns have no independent object labels.")
    add("opposed-gliders", GLIDER + [(7-y, 7-x) for y, x in GLIDER], None,
        "diagnostic", limitation="Engineered encounter challenge; no collision/product tracking is implemented.")
    for seed in (7, 11):
        rng = np.random.Generator(np.random.PCG64(seed))
        initial = (rng.random((32, 32)) < 0.25).astype(np.uint8)
        add(f"clutter-seed-{seed}", [], None, "diagnostic", initial=initial,
            seed=seed, density=0.25, rng="PCG64",
            limitation="Unlabelled clutter; a recurrence result would not identify an autonomous object.")
    return panel


def confusion(rows, key):
    scored = [r for r in rows if r["label"] is not None and r["status"] == "ok"]
    counts = {"tp": 0, "fp": 0, "tn": 0, "fn": 0}
    for row in scored:
        label, pred = row["label"], row[key]
        counts["tp" if label and pred else "fn" if label else "fp" if pred else "tn"] += 1
    tp, fp, tn, fn = (counts[k] for k in ("tp", "fp", "tn", "fn"))
    ratio = lambda n, d: n / d if d else None
    return {**counts, "n_scored": len(scored),
            "n_errors": sum(r["status"] != "ok" for r in rows),
            "precision": ratio(tp, tp+fp), "recall": ratio(tp, tp+fn),
            "false_positive_rate": ratio(fp, fp+tn), "accuracy": ratio(tp+tn, len(scored))}


def run_pilot(protocol: Path):
    started = time.perf_counter()
    output = {"experiment_id": "CE-001", "protocol_version": "pilot-v1",
              "status": "engineered-assay-pilot-not-general-object-validation",
              "protocol_sha256": hashlib.sha256(protocol.read_bytes()).hexdigest(),
              "provenance": source_provenance(), "rule": "B3/S23", "boundary": "periodic",
              "shape": [32, 32], "hash_encoding": "C-order uint8 bytes", "cases": []}
    for case in cases():
        initial = case["initial"]
        row = {k: v for k, v in case.items() if k != "initial"}
        row.update({"initial_live_cells": np.argwhere(initial).tolist(),
                    "initial_sha256": state_hash(initial)})
        try:
            found = exact_translational_recurrence(initial, case["max_period"], case["max_shift"])
            row.update({"status": "ok", "recurrence": asdict(found) if found else None,
                        "assay": found is not None, "occupancy_baseline": bool(initial.any()),
                        "stationarity_baseline": bool(initial.any()) and np.array_equal(life_step(initial), initial)})
        except Exception as exc:  # Preserve failures alongside successful/negative cases.
            row.update({"status": "error", "error": f"{type(exc).__name__}: {exc}"})
        output["cases"].append(row)
    output["metrics"] = {}
    for split in ("development", "held-out", "combined"):
        rows = [r for r in output["cases"] if r["label"] is not None and
                (split == "combined" or r["split"] == split)]
        output["metrics"][split] = {key: confusion(rows, key) for key in
                                   ("assay", "occupancy_baseline", "stationarity_baseline")}
    output["elapsed_seconds"] = time.perf_counter() - started
    output["passed_fixture_expectations"] = not any(
        r["status"] != "ok" or (r["label"] is not None and r["assay"] != r["label"])
        for r in output["cases"])
    return output


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--protocol", type=Path,
                        default=Path(__file__).resolve().parents[2] / "experiments/CE-001/pilot-v1.md")
    args = parser.parse_args(argv)
    if args.output.exists():
        parser.error("output already exists; preserve prior results and choose another path")
    result = run_pilot(args.protocol)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if not result["passed_fixture_expectations"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
