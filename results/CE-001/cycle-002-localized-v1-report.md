# Cycle 002: conservative localized recurrence candidates

The assay recovered **13 of 16 supplied analytic objects**, with no unmatched
predictions, across 14 scored engineered trajectories. It recovered separate
stationary/moving structures and oppositely moving gliders where the full grid
does not recur under one translation. It deliberately missed two nearby stable
blocks and a disconnected oscillator phase; all three false negatives remain in
the denominators. Six additional diagnostic trajectories remain unlabelled and
unscored. These observations validate a limited geometric method on selected
fixtures; they do not identify physical individuals or test H1–H3.

## Method and prespecification

The [protocol](../../experiments/CE-001/cycle-002-localized-v1.md), detector,
case constructions, expected analytic footprints/signatures, tests and scoring
were frozen at `af942f85f5682e7d2fc330dacf9b53f2351d91e5` before execution.
An independent Critical Reviewer agent inspected this exact protocol/code before
seeing benchmark outputs and found no blocking methodology issue. No evaluation
case, threshold or label changed after observation.

The detector consumes the unlabelled Life trajectory and fixed numerical limits;
it has no pattern dictionary or ground-truth access. It segments live cells by
radius-two proximity, requires an initially eight-connected support, verifies
that isolated evolution exactly matches a unique observed component at every
frame, and requires exact initial-state recurrence plus two observed cycles.
It abstains on segmentation ambiguity, mismatched interactions, edge proximity,
oversize supports, missing recurrence or short windows. Every t=0 support gets
a disposition. It does not track structures born after t=0.

Ground truth consists of supplied analytic block/blinker/glider/toad footprints
and their known periods/displacements. Nearby independent blocks and the toad's
other phase have positive truth even though they violate the detector's initial
segmentation convention. They are therefore real method misses relative to this
panel's object-inventory task, rather than removed as inconvenient examples.
Unit tests verify known cycles, the nearby blocks' combined stationarity and the
different treatment of the toad's two phases.

All cases use periodic Life B3/S23, 48×48 grids, and 12 updates except the two-step
short-window diagnostic. Limits are period ≤4, translation coordinates −2…2,
bounding spans ≤8, edge margin 2 and at least two observed periods. The same
observed-cycle constraint applies to the whole-grid baseline. Full parameters,
live-cell coordinates, every frame's hash, source hashes, clean execution SHA,
Python/NumPy versions and protocol SHA-256 are in
[the complete output](cycle-002-localized-v1.json).

## Exact object matching and baseline results

A match requires exact initial footprint, least period and displacement, with
one-to-one assignment. A merged footprint or wrong signature produces both an
unmatched prediction and missed truth. Abstention on a labelled positive produces
false negatives. Object-count error is also reported because counting correctly
does not imply identifying the right structures.

| Method | TP | FP | FN | Precision | Recall | Mean absolute count error |
|---|---:|---:|---:|---:|---:|---:|
| Localized candidates | 13 | 0 | 3 | 13/13 | 13/16 | 3/14 |
| Whole-grid recurrence proxy | 7 | 1 | 9 | 7/8 | 7/16 | 8/14 |
| Occupancy-static proxy | 1 | 12 | 15 | 1/13 | 1/16 | 7/14 |

The occupancy proxy guesses one stationary component from every nonempty grid.
The whole-grid proxy proposes the entire recurrent live set as one component.
These deliberately simple inventory proxies do not segment multiple objects;
their poor signature-matching scores do not mean global recurrence is useless.
The whole-grid method correctly identifies the disconnected-phase toad that the
localized method misses. The localized method's count error is better here, but
occupancy can guess the right count while missing the footprint or motion.

| Scored case | Truth objects | Localized TP/FP/FN | Whole-grid TP/FP/FN |
|---|---:|---|---|
| block | 1 | 1/0/0 | 1/0/0 |
| blinker | 1 | 1/0/0 | 1/0/0 |
| glider | 1 | 1/0/0 | 1/0/0 |
| toad | 1 | 1/0/0 | 1/0/0 |
| stationary-plus-moving | 2 | 2/0/0 | 0/0/2 |
| two-different-velocities | 2 | 2/0/0 | 0/0/2 |
| empty | 0 | 0/0/0 | 0/0/0 |
| single-transient | 0 | 0/0/0 | 0/0/0 |
| pair-transient | 0 | 0/0/0 | 0/0/0 |
| reflected-translated-glider | 1 | 1/0/0 | 1/0/0 |
| rotated-translated-toad | 1 | 1/0/0 | 1/0/0 |
| three-separated | 3 | 3/0/0 | 0/0/3 |
| nearby-independent-blocks | 2 | 0/0/2 | 0/1/2 |
| phase-shifted-toad | 1 | 0/0/1 | 1/0/0 |

Development results: 8 TP, 0 FP, 0 FN across nine scored trajectories.
Held-out results: 5 TP, 0 FP, 3 FN across five scored trajectories, recall 5/8.
The implementation author knew all fixtures and labels; `held-out` means fixed
transformations/limitations excluded from tuning, not independent authorship.
The three zero-truth trajectories produced no false localized/whole-grid
prediction; occupancy produced a false prediction in two of three.

E1 (exact recovery in the stated isolation regime), E2 (different-motion recovery
beyond one global translation), and E3 (specified boundary/window/encounter
abstentions) passed. This narrowly scoped acceptance flag does not erase the
three false negatives outside that regime or imply full-panel perfect recall.
There were no case exceptions, test failures, pilot retries or timeout failures.
The single pilot completed in approximately 0.235 seconds; runtime is descriptive.

## Diagnostic and negative evidence

All six unlabelled diagnostics emitted zero localized candidates. This does not
establish absence of objects; unknown truth lists have `evaluation: null` and
are excluded from supervised precision/recall. Every raw baseline prediction and
initial component's failure reason/frame remains archived.

| Diagnostic | Recorded localized disposition |
|---|---|
| short-window-blinker | One abstention at frame 2: insufficient observed cycles |
| periodic-edge-glider | Four edge-fragment abstentions at frame 0; no unwrapping attempted |
| overlapping-engineered-blocks | One transient rejection at frame 2 |
| opposed-glider-encounter | Both initial supports abstain at frame 7: interaction or segmentation change |
| clutter-seed-13 | All initial supports abstain/reject; no labelled object-free assertion |
| clutter-seed-17 | All initial supports abstain/reject; no labelled object-free assertion |

The nearby-block miss demonstrates overmerging by the radius-two isolation
guard. The phase-shifted-toad miss demonstrates dependence on initial connectivity
and observation phase. These are substantive limits, not simulation errors.
Boundary fragment counts describe the nonperiodic segmentation convention and
must not be interpreted as counts of physical glider components.

## Reproduction and verification

Original execution: clean Git revision
`af942f85f5682e7d2fc330dacf9b53f2351d91e5`, Python 3.12.14, NumPy 2.5.5.
The output contains the SHA-256 of the frozen protocol and each Python source.
The dependency snapshot is
[cycle-002-requirements.txt](../../experiments/CE-001/cycle-002-requirements.txt).
Install that list from the result commit into a separate worktree and install
the project itself there. For the exact source revision:

```bash
git worktree add /tmp/ce002-reproduction af942f85f5682e7d2fc330dacf9b53f2351d91e5
cd /tmp/ce002-reproduction
python -m venv .venv
.venv/bin/python -m pip install -e '.[dev]' numpy==2.5.5 pytest==9.2.0
env PYTHONPATH=src .venv/bin/pytest -q
timeout 300s env PYTHONPATH=src .venv/bin/python -m compositional_emergence.benchmark_localized --output /tmp/ce002-reproduction.json
```

The complete suite passed **42 tests** in 0.36 seconds. New checks cover separated
moving/static recovery, analytic cycles, disclosed segmentation misses, one-to-one
matching under duplicates/wrong signatures, invalid temporal data and limits,
boundary/short-window abstention, case/split counts and evidence preservation.
Existing independent scalar Life and exhaustive ECA rule checks also pass.
Compare source/protocol hashes, fixture coordinates, trajectory hashes, tracks,
signatures, matching indices, metrics and expectations; runtime and Git dirty
metadata may differ. Existing output paths are refused with exclusive creation.

## Scope of inference and handoff

The sampling unit is an engineered trajectory, never a frame. Exact counts and
fractions describe this selected panel; no population confidence interval or
general object-detection performance estimate is justified. No finite-size sweep,
stochastic sample, object annotation study, new-rule exploration or significance
test was performed. A matched isolated evolution is a finite geometric witness,
not a causal-autonomy, object-identity or compositional-product certificate.

Independent source/method review and rerun are tracked in the governance audit.
The implementation workstream stops at this submitted cycle. No merge, Stage C,
H1–H3 test, new research cycle or scientific novelty claim is authorized here.
