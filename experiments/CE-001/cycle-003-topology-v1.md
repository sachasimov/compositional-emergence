# CE-001 cycle 003: overlap-connected topology v1

Date: 2026-11-18. Baseline `aeed31d4487908029b0107f253f8329a795a78cd`.
Freeze this protocol, implementation, analytic labels, evaluation and tests in a
commit, obtain independent methodological preflight, then execute the fixed
benchmark once. This is engineered Stage B validation in the single approved
cycle 003. All earlier protocols, methods and outputs remain unchanged.

## Question, method and competing explanation

Can a generic spacetime grouping recover the three scored cycle-002 misses
(two nearby stationary blocks and a disconnected toad phase), while preserving
known isolated recovery and exposing geometric decomposition ambiguity?

The versioned `localized_v2.py` method consumes only binary Life trajectories
and fixed limits, with no pattern dictionary, fixture IDs, expected labels or
fitted parameters:

1. Segment every frame into ordinary-coordinate eight-connected live supports.
2. Between consecutive frames, connect components if they share at least one
   live-cell coordinate. Take connected components of this spacetime graph.
   Each observed spatial component belongs to exactly one graph group. Thus
   groups' same-frame supports are disjoint; duplicate/overlapping candidate
   proposals cannot be produced by this construction.
3. For each whole graph group, take the union of its live cells in every frame.
   Groups without any t=0 support receive an explicit `no-window-start-support`
   abstention. The method does not infer or track the identity of later births.
4. Independently evolve the entire initial support alone under Life. It must
   equal the **complete observed graph group** at every frame, never a selected
   favorable subset. Extinction, disagreement, boundary proximity, excessive
   span, missing recurrence or insufficient observation yields a recorded
   rejection/abstention for that group.
5. As in cycle 002, require a least initial-state translational recurrence with
   period ≤4, shifts −2…2, two observed whole periods, edge margin 2 and bounding
   span ≤8. Inputs must satisfy Life at each transition. Return initial footprint,
   exact period/displacement and all group support hashes/dispositions.

The entire observation window determines grouping. Split/merge graph association
is not a causal edge or a certificate of interaction/identity. It may join the
disconnected phases of one oscillator or falsely fuse supplied independent
objects. Matching isolated evolution certifies only finite geometric agreement.
No unique object decomposition, autonomy, closure, lineage or composition follows.
Persistent structures with **no shared live coordinates between consecutive
frames** may be split into separate groups and missed; the association rule does
not cover every motion or oscillator. Initial recurrence, phase, size, observation
length and nonperiodic segmentation remain restrictive assumptions.

## Falsifiable expectations

- E1: Recover all three previously recorded misses with exact supplied initial
  footprints, least periods and displacements, with no extra predictions on the
  two development-regression trajectories. Any mismatch falsifies this repair
  expectation. These are known failures, not untouched discovery cases.
- E2: Recover all labelled objects without extras in the remaining declared
  isolated regression/prospective cases, excluding only the explicitly scored
  decomposition-ambiguity challenge. Any mismatch falsifies E2 here.
- E3: Emit no complete v2 candidate on boundary, insufficient-window or engineered
  encounter diagnostics. Any such output falsifies E3; preserve it regardless.

The competing explanation is that the previous detector or the no-split/merge
association ablation already recovers these cases as well. Report their exact
scores on identical inputs rather than selecting a favorable old benchmark.
No statistical significance or general detector superiority is claimed.

The adjacent-tub case remains scored with two supplied independent stationary
supports, even if all methods emit one recurrent composite. Its unmatched
composite is an FP and both missed supports are FNs. This deliberately tests
the ambiguity of the geometric inventory convention and stays in all full-panel
metrics. The narrow E1–E3 acceptance flag does not mean perfect overall performance.

## Cases, labels and split definitions fixed before results

All grids are 48×48, periodic Life B3/S23 with synchronous updates. The default
horizon is 12 updates; short-window cases use two. Exact coordinates, offsets,
analytic glider/toad phases and expected signatures are fixed in
`benchmark_topology.py`. Labels come from supplied finite pattern cycles and
mathematically checked stationary decompositions, never the evaluated graph.

**Development regressions:** rerun all 14 scored cycle-002 trajectories, including
its old transformed cases, with identical coordinates/horizons/truth. Relabel
every one as development and retain original split metadata. These contain 16
supplied truth objects, including the three prior misses. Reuse its six unlabelled
diagnostics unchanged; no result-based deletion or relabelling is permitted.

**Prospective fixed extension:** the implementation author knows all constructions
and labels. This is a frozen prospective sensitivity panel, not an independently
authored or statistically independent held-out dataset.

| Cases | Count | Independent supplied truth |
|---|---:|---|
| Translated glider phases 0,1,2,3 | 4 | One period-4 spaceship each, displacement (1,1); phase coordinates explicit |
| Rotated/translated toad phases 0,1 | 2 | One period-2 oscillator each, displacement (0,0) |
| Translated vertical blinker | 1 | One period-2 oscillator |
| Horizontal block start spacings 3,4,6 | 3 | Two independent stationary blocks each; spaces contain 1,2,4 empty columns |
| Vertical start spacing 3 and diagonal offset (3,3) | 2 | Two independent stationary blocks each |
| Single tub | 1 | One stationary four-cell support |
| Diagonally adjacent tubs | 1 | Two individually stationary tubs at offsets (20,20),(22,22); union also stationary and eight-connected |
| Disconnected-phase toad plus translated phase-1 glider | 1 | Two independently evolving separated objects |

These add 15 scored trajectories and 22 supplied objects: **29 scored trajectories,
38 supplied objects in total**. The two-tub decomposition is explicitly conventional:
both parts and their union are stationary, so Life alone does not certify that the
two-part inventory is uniquely physically correct. Unit/reference checks verify
the supplied cycles and every stationary combined block/tub construction.

**Additional diagnostics:** disconnected-phase toad with only two updates;
boundary-adjacent disconnected toad; three separated parent cells at
(20,20),(20,22),(22,20) whose only live child is (21,21) at t=1 and then extinction.
The last case ensures groups lacking t=0 support are excluded explicitly. These
three add to the six original diagnostics: **38 trajectories total**, including
nine unlabelled diagnostics with `evaluation: null`. Unknown diagnostic truth is
never interpreted as zero true objects or added to precision/recall denominators.

## Baselines, matching and metrics

Run all three methods on the same complete trajectory, same horizon, observation
budget, recurrence/shift/localization bounds, rule and environment:

1. **v2 overlap union:** all temporal shared-coordinate edges.
2. **Previous localized v1:** unchanged `localized.detect_candidates`, including
   radius-two grouping, initial eight-connectivity and its original context test.
3. **One-to-one overlap ablation:** identical v2 geometry, frame access, group
   validation and recurrence checks, changing **only** temporal association. Keep
   an overlap edge across a transition only when both component endpoints have
   degree one across that transition. This segmentation-association baseline
   forbids split/merge grouping; its resulting no-t=0 groups are also excluded.

No full-grid/occupancy proxy is used as the only comparator in this cycle.
One-to-one association is deliberately narrower than general phase tracking;
its failures quantify this particular edge-choice ablation, not every alternative
tracking method or causal reconstruction.

Use the existing exact one-to-one matching: exact initial live-cell footprint,
least period and displacement, each supplied truth and prediction at most once.
Merged/split/wrong-signature predictions count as FP plus missed truth FNs.
Abstentions on labelled positives count as FNs. Archive each match/unmatched index,
TP/FP/FN, predicted/truth counts and absolute count error. Report per split and
combined precision TP/(TP+FP), recall TP/(TP+FN), count MAE per scored trajectory,
case errors, and false predictions on zero-truth trajectories. Null denominators
remain null. Report every group's acceptance/rejection/abstention reason, first
failure frame, spatial-component counts and hashes, including all nine diagnostics.
Also report candidate/abstention coverage and the scored composite-fusion error.

Sampling units are selected engineered trajectories and supplied object supports,
not adjacent frames. Exact fractions/denominators describe this panel; no iid
population confidence interval or inferential significance is appropriate.

## Execution, provenance, resource cap and stop

Record the protocol SHA-256, source-file hashes, clean execution Git SHA/dirty
status, Python/NumPy versions, full initial cells/parameters, every frame hash,
all predictions, dispositions, matches, exceptions and timing. Output creation is
exclusive and existing paths are rejected. Preserve all cases after a failed
expectation; exit nonzero on any expectation failure or case exception. Never
retry to improve scores or tune to observed outcomes.

After frozen-SHA preflight:

```bash
env PYTHONPATH=src /workspace/ce-simulation/.venv/bin/pytest -q
timeout 300s env PYTHONPATH=src /workspace/ce-simulation/.venv/bin/python -m compositional_emergence.benchmark_topology --output results/CE-001/cycle-003-topology-v1.json
```

One fixed benchmark, <5 CPU minutes, no paid compute, rule/seed/target search or
spontaneous discovery. Record a timeout as a failed attempt. Independent audit
reproductions and explicit in-cycle repair amendments are allowed; preserve the
original protocol and outputs. No Stage C, H1–H3 experiment, scientific novelty
claim, merge, cycle 004 or further research cycle is authorized. Stop after
independent critical review and PR handoff to the human.
