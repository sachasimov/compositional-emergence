"""Reproducible reference simulation CLI; no scientific inference."""
import argparse
import json
from pathlib import Path
import numpy as np
from . import __version__
from .automata import eca_step, life_step
from .provenance import source_provenance, state_hash

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run a baseline CA trajectory")
    parser.add_argument("--system", choices=("life", "eca"), required=True)
    parser.add_argument("--rule", type=int, default=110)
    parser.add_argument("--size", type=int, default=40)
    parser.add_argument("--steps", type=int, default=20)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--density", type=float, default=0.25)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args(argv)
    if args.size < 3 or args.steps < 0 or not 0 <= args.density <= 1:
        parser.error("size >=3, steps >=0 and density in [0,1] are required")
    if args.system == "eca" and not 0 <= args.rule <= 255:
        parser.error("ECA rule must lie in [0,255]")
    if args.seed < 0:
        parser.error("seed must be nonnegative")
    if args.output is not None and args.output.exists():
        parser.error("output already exists; preserve prior results and choose another path")
    rng = np.random.Generator(np.random.PCG64(args.seed))
    shape = (args.size, args.size) if args.system == "life" else (args.size,)
    state = (rng.random(shape) < args.density).astype(np.uint8)
    initial = state.copy()
    counts = [int(state.sum())]
    for _ in range(args.steps):
        state = life_step(state) if args.system == "life" else eca_step(state, args.rule)
        counts.append(int(state.sum()))
    result = {
        "status": "baseline-simulation-not-a-scientific-result",
        "package_version": __version__, "system": args.system,
        "rule": "B3/S23" if args.system == "life" else args.rule,
        "boundary": "periodic", "shape": list(shape), "seed": args.seed,
        "initial_density": args.density, "steps": args.steps,
        "population_counts": counts
    }
    result.update({"manifest_version": "CE-001-stage-a-v1",
                   "provenance": source_provenance(), "rng": "PCG64",
                   "initial_state": initial.tolist(), "initial_state_sha256": state_hash(initial),
                   "final_state": state.tolist(), "final_state_sha256": state_hash(state),
                   "hash_encoding": "C-order uint8 bytes; shape recorded separately"})
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output is None:
        print(encoded, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        try:
            with args.output.open("x", encoding="utf-8") as stream:
                stream.write(encoded)
        except FileExistsError:
            parser.error("output already exists; preserve prior results and choose another path")

if __name__ == "__main__":
    main()
