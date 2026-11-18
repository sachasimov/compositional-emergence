# CE-001 cycle 002: localized recurrence candidates v1

Date: 2026-11-18. Baseline `18c7beff8f60ff60e28b81db2b9ac1250127e099`.
Freeze this protocol, case table, implementation and evaluation in a commit
before benchmark execution. This is the single approved bounded cycle 002,
engineered Stage B method validation, not Stage C, H1–H3 or a novelty test.
Cycle-001 protocols and outcomes remain unchanged.

## Definition and limitations fixed before observation

A **window-start localized recurrence candidate** is a finite live-cell support
present at the first frame, meeting all of the following geometric criteria:

1. Segment each frame into Chebyshev-radius-two connected live-cell supports,
   using ordinary coordinates without periodic unwrapping. Radius two is a
   conservative isolation guard for overlapping Life neighborhoods.
2. An initial support must also be eight-connected. Multiple eight-connected
   pieces within one radius-two component cause initial-segmentation abstention.
3. Evolve the initial component alone under the declared Life rule. At every
   observed frame, this isolated evolution must equal exactly one whole observed
   radius-two component. Contact/merging/splitting or an unmatched support causes
   abstention for the entire window. Extinction is recorded as transient rejection.
4. Every tracked support must remain at least two cells from every grid edge and
   have bounding-box spans at most eight cells. Otherwise abstain. No unwrapping
   or physical individual inference is attempted.
5. The initial support must recur under a single translation with least period
   at most four and each displacement coordinate in −2…2, using existing exact
   assay tie-breaking. Require at least two whole observed periods. A candidate
   has its exact initial footprint, period and displacement, plus per-frame
   support hashes. The complete input must satisfy the Life update rule.

This is an intentionally narrow, phase-dependent segmentation convention. It
misses nearby independent objects, some disconnected oscillator phases, births
after the window start, long-period objects and objects undergoing encounters.
Recurrence and isolation do not establish physical autonomy, causal closure or
composition. The implementation uses no pattern dictionary or expected labels.

## Falsifiable expectations and competing explanation

- E1: In the declared isolation regime, recover every supplied analytic object's
  exact initial footprint, least period and displacement, with no extra objects;
  return no candidates for empty or extinguishing fixtures. Any unmatched truth
  or prediction in that regime falsifies E1 on this panel.
- E2: For the stationary-plus-moving and two-different-velocities cases, match
  more truth objects than the whole-grid assay proxy. Failure in either case
  falsifies E2. The competing explanation is that one global translation already
  suffices for these engineered trajectories.
- E3: Emit no complete isolated candidate for the insufficient-window, boundary
  and engineered encounter challenges. Any such candidate falsifies E3 here.
  Preserve all diagnostic outputs regardless of expectation outcomes.

Two known segmentation-limit cases remain **scored** with independent positive
truth, even though the conservative method is expected to miss them. Their false
negatives cannot be removed to improve recall. The acceptance flag evaluates the
three narrow expectations above, not a claim of perfect full-panel performance.

## Fixed cases and labels

All grids are 48×48, periodic Life B3/S23, synchronous updates. Default horizon is
12 steps/13 frames. Analytic pattern coordinates and offsets, expected periods
and displacement vectors are explicitly supplied in `benchmark_localized.py`.
Ground truth is the supplied fixture construction plus the known finite pattern
cycles, never the detector's segmentation or outputs. Analytic expected behavior
is checked in unit/reference tests. No label fitting or threshold selection occurs.

| Split | Cases | Independent truth |
|---|---|---|
| Development, scored | block, blinker, glider, toad | One object each: periods 1,2,4,2; glider displacement (1,1), others (0,0) |
| Development, scored | stationary-plus-moving | Separated block and SE glider, two objects |
| Development, scored | two-different-velocities | Separated SE and NW gliders moving apart, two objects, period 4, displacements (1,1), (−1,−1) |
| Development, scored | empty, single-transient, pair-transient | Zero persistent initial objects |
| Held-out, scored | reflected-translated-glider, rotated-translated-toad | One object each, period 4/(1,−1) and period 2/(0,0) |
| Held-out, scored | three-separated | Block, blinker and SW glider, three objects |
| Held-out, scored limitation | nearby-independent-blocks | Two stationary blocks with one empty column between; their combined field is stationary despite conservative grouping |
| Held-out, scored limitation | phase-shifted-toad | One period-two toad in its disconnected initial phase |
| Diagnostic, unscored | short-window-blinker | Known oscillator, only two steps; abstain for insufficient cycles |
| Diagnostic, unscored | periodic-edge-glider | Known spaceship crossing edge; abstain under boundary convention |
| Diagnostic, unscored | overlapping-engineered-blocks | Unlabelled object identity; do not infer product objects |
| Diagnostic, unscored | opposed-glider-encounter | Unlabelled encounter/product identity; no complete isolated track |
| Diagnostic, unscored | clutter-seed-13, clutter-seed-17 | PCG64, density 0.12; unlabelled, never assumed object-free |

There are 14 scored trajectories with 16 supplied truth objects and 6 diagnostic
trajectories. Held-out means specified transformations/limitations excluded from
tuning, not independent authorship: the implementation author knows all fixtures
and labels. No frames are counted as independent samples. No rule/seed search or
later spontaneous initializations are permitted in this cycle.

## Matching, baselines and reporting

Match a prediction to at most one truth object by exact t=0 footprint **and** exact
least period/displacement. Greedy exact matching in prediction order is unique
for distinct supplied supports; duplicate predictions can match at most once.
Wrong signature or merged/split footprints yield an unmatched prediction (FP)
and unmatched truth (FN). TP/FP/FN, matching indices, unmatched indices, predicted
and truth counts, and absolute count error are archived for every scored case.
Abstentions produce no prediction and therefore incur FNs for every missed truth.

Report micro precision TP/(TP+FP), recall TP/(TP+FN), mean absolute object-count
error per scored trajectory, and the number of the three zero-truth trajectories
with any false prediction. Undefined ratios are null. Report development,
held-out and combined results, errors and exact denominators. No statistical
population confidence intervals: fixtures are selected, dependent constructions.

Apply identical exact matching and count metrics to two intentionally simple
proxies on the same scored cases and same observation budget:

- **Whole-grid assay:** if the entire nonempty initial grid recurs with period
  ≤4, shift bound 2 and at least two observed periods, emit one candidate whose
  footprint is the entire initial live set and whose signature is that recurrence.
- **Occupancy-static:** emit one candidate for any nonempty initial grid, guessing
  period 1/displacement (0,0), with its whole-grid live set as footprint.

These are candidate-inventory proxies, not segmentation algorithms. Their merged
footprints/guessed signatures can fail exact matching even if they detect useful
global regularity. Count error is also reported to make this task mismatch clear.
No significance or superiority beyond these fixtures is implied.

Every initial component's accepted/rejected/abstained disposition and reason,
first failure frame, candidate signature, support hashes, every diagnostic
prediction, all errors and unexpected outputs are preserved. Diagnostics have
explicit `evaluation: null`; empty diagnostic truth lists mean unavailable
labels, not zero ground-truth objects. Report diagnostic candidate counts and
abstention reasons separately rather than hiding them behind primary metrics.

## Execution, resource and stop rules

Use the existing local virtual environment or install the project development
requirements in a fresh one. Ensure imports point to this worktree. Record
Python/NumPy versions, all source hashes, exact Git revision/dirty status,
protocol hash, full initial coordinates, generation parameters and every frame's
hash in the output. Refuse existing output paths; exclusive creation prevents
overwriting evidence. Execute once after preflight review:

```bash
PYTHONPATH=src /workspace/ce-simulation/.venv/bin/pytest -q
timeout 300s env PYTHONPATH=src /workspace/ce-simulation/.venv/bin/python -m compositional_emergence.benchmark_localized --output results/CE-001/cycle-002-localized-v1.json
```

Budget: one fixed 20-case benchmark, CPU only, <5 minutes, no paid compute. Record
every case even after a mismatch/exception; exit nonzero when E1–E3 fail or any
exception occurs. A timeout is a failed attempt and must be logged. No retries
to improve scores. Independent audit reproductions and documented fixes are
allowed within this cycle; preserve the original protocol/output and explicitly
record amendments. Stop after archived outcomes, independent review and PR
handoff. No merge, Stage C, next research cycle or H1–H3 experiment is authorized.
