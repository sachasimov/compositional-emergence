# Cycle 003: spacetime grouping repairs phase/proximity misses, but still fuses a supplied decomposition

The versioned geometric method recovers the **three known cycle-002 misses** and
matches **36 of 38 supplied object supports** across 29 scored engineered
trajectories. It also emits **one false composite and misses both supplied tubs**
in the fixed decomposition challenge. The unchanged previous method matches
25/38 supports; an association-only ablation matches 30/38. All comparisons use
identical input trajectories and matching rules. These are finite geometric
inventory results relative to explicit labels, not physical individuation or
evidence for H1–H3, composition, causal autonomy or scientific novelty.

## Frozen design and independent preflight

Baseline `aeed31d4487908029b0107f253f8329a795a78cd` contains audited cycle-002
work. The new [protocol](../../experiments/CE-001/cycle-003-topology-v1.md),
versioned detector, case constructions, analytic labels, ablation and tests were
committed at `93a1f52479587b1cd5ef13957c200fbddb214bb5` before the benchmark.
The Critical Reviewer agent inspected this exact revision without seeing pilot
outputs and found no blocking methodology issue. The benchmark then ran once
from that clean revision; no parameters, cases, labels or implementation changed
after observation. Earlier methods, protocols and results remain unchanged.

The new method segments each frame into eight-connected supports and links
consecutive supports sharing live-cell coordinates. Connected components of this
spacetime graph can join the disconnected phases of one oscillator without
joining nearby stationary blocks. Each graph group is disjoint from all others
at every frame. A group with no t=0 support is explicitly excluded. For the
remaining groups, isolated evolution of the complete initial support must equal
the **complete observed group at every frame**; no favorable subset is selected.
The same finite recurrence, observation, boundary and size limits then apply.

This is an offline whole-window grouping convention. Graph connectivity may
merge objects through future contact or spatial adjacency, and it can miss
motions/oscillators with no shared live coordinates between consecutive frames.
Its edges are bookkeeping associations, not causal links. An exactly matching
isolated evolution is a finite witness of geometric agreement, not proof of a
unique internal decomposition or autonomous identity.

## Truth, cases and matching

All 14 original scored cycle-002 cases are **development regressions**, including
its previously named held-out transformations. Their original metadata is
retained, and all three known misses remain positive truth. Fifteen new fixed
prospective cases test explicit glider/toad phases, translation, orientation,
block spacing, a new stationary tub, and separated multipart/moving structures.
Nine diagnostics retain unresolved labels and have `evaluation: null`.

Truth consists of supplied analytic initial footprints and least-period/
displacement signatures, not detector outputs. Independent scalar Life reference
checks verify the explicit four-phase glider cycle, stationary block constellations,
each supplied tub and their stationary union. The two-tub inventory is a stated
conventional decomposition: its parts and their union are stationary, so these
dynamics do not uniquely distinguish the two-part inventory from one composite.
The challenge is nevertheless scored consistently against its frozen two-support
labels; an emitted union receives an FP and two missed-part FNs.

The author knew all constructions and labels. Prospective means fixed before
results; it is not independent authorship, blinded testing or a random sample.
No label was inferred from segmentation. Exact one-to-one matching requires the
initial footprint **and** least period/displacement. Wrong or merged predictions
generate FP/FNs; abstention on a labelled positive incurs an FN. Object-count
error is reported separately because the right count can still hide wrong parts.

## Same-input baseline and ablation

All three methods consume the same 48×48 periodic Life B3/S23 trajectories,
normally 12 updates/13 frames, with period ≤4, displacement coordinates −2…2,
two observed periods, edge margin 2 and span bound 8:

- **Spacetime v2:** all temporal shared-coordinate overlap edges.
- **Localized v1:** the unchanged cycle-002 radius-two detector, executed directly
  on each current input rather than selecting an old result.
- **One-to-one overlap ablation:** the same v2 segmentation, observation budget,
  group verification and recurrence checks; change only temporal edge selection.
  An edge survives only if each endpoint has degree one across that transition.
  Thus split/merge association is disabled without giving v2 extra frames or truth.

| Method | TP | FP | FN | Precision | Recall | Count MAE per trajectory |
|---|---:|---:|---:|---:|---:|---:|
| Spacetime v2 | 36 | 1 | 2 | 36/37 | 36/38 | 1/29 |
| Previous localized v1 | 25 | 1 | 13 | 25/26 | 25/38 | 12/29 |
| One-to-one overlap ablation | 30 | 1 | 8 | 30/31 | 30/38 | 7/29 |

| Split | Method | TP/FP/FN | Count MAE |
|---|---|---|---|
| Development, 14 trajectories/16 supports | v2 | 16/0/0 | 0/14 |
| Development | v1 | 13/0/3 | 3/14 |
| Development | ablation | 13/0/3 | 3/14 |
| Prospective, 15 trajectories/22 supports | v2 | 20/1/2 | 1/15 |
| Prospective | v1 | 12/1/10 | 9/15 |
| Prospective | ablation | 17/1/5 | 4/15 |

The unchanged v1 reproduces its cycle-002 outcomes on all original cases. The
nearby block improvement arises from avoiding radius-two overgrouping: both v2
and the one-to-one ablation recover those blocks. The disconnected-phase toad
needs split/merge association: v2 recovers it while the ablation abstains. The
ablation also misses the connected initial toad phase once its later phase
splits. This identifies the tested association choice's role without claiming
superiority over every alternative tracker or causal reconstruction.

All three methods return a single composite for the diagonal-tub pair. V2's
higher recovery elsewhere does not repair this decomposition ambiguity. The
false composite, two FNs and one-count error remain in all prospective/full-panel
scores. No false predictions occurred on the three scored zero-truth development
trajectories; the prospective split contains no zero-truth cases.

## Per-case recovery and preserved errors

Development regressions:

| Case | Truth supports | v2 TP/FP/FN | v1 TP/FP/FN | Ablation TP/FP/FN |
|---|---:|---|---|---|
| block | 1 | 1/0/0 | 1/0/0 | 1/0/0 |
| blinker | 1 | 1/0/0 | 1/0/0 | 1/0/0 |
| glider | 1 | 1/0/0 | 1/0/0 | 1/0/0 |
| toad | 1 | 1/0/0 | 1/0/0 | 0/0/1 |
| stationary-plus-moving | 2 | 2/0/0 | 2/0/0 | 2/0/0 |
| two-different-velocities | 2 | 2/0/0 | 2/0/0 | 2/0/0 |
| empty | 0 | 0/0/0 | 0/0/0 | 0/0/0 |
| single-transient | 0 | 0/0/0 | 0/0/0 | 0/0/0 |
| pair-transient | 0 | 0/0/0 | 0/0/0 | 0/0/0 |
| reflected-translated-glider | 1 | 1/0/0 | 1/0/0 | 1/0/0 |
| rotated-translated-toad | 1 | 1/0/0 | 1/0/0 | 0/0/1 |
| three-separated | 3 | 3/0/0 | 3/0/0 | 3/0/0 |
| nearby-independent-blocks | 2 | 2/0/0 | 0/0/2 | 2/0/0 |
| phase-shifted-toad | 1 | 1/0/0 | 0/0/1 | 0/0/1 |

Prospective fixed checks:

| Case | Truth supports | v2 TP/FP/FN | v1 TP/FP/FN | Ablation TP/FP/FN |
|---|---:|---|---|---|
| glider phase 0 | 1 | 1/0/0 | 1/0/0 | 1/0/0 |
| glider phase 1 | 1 | 1/0/0 | 1/0/0 | 1/0/0 |
| glider phase 2 | 1 | 1/0/0 | 1/0/0 | 1/0/0 |
| glider phase 3 | 1 | 1/0/0 | 1/0/0 | 1/0/0 |
| rotated toad phase 0 | 1 | 1/0/0 | 1/0/0 | 0/0/1 |
| rotated toad phase 1 | 1 | 1/0/0 | 0/0/1 | 0/0/1 |
| vertical blinker | 1 | 1/0/0 | 1/0/0 | 1/0/0 |
| horizontal block spacing 3 | 2 | 2/0/0 | 0/0/2 | 2/0/0 |
| horizontal block spacing 4 | 2 | 2/0/0 | 2/0/0 | 2/0/0 |
| horizontal block spacing 6 | 2 | 2/0/0 | 2/0/0 | 2/0/0 |
| vertical near blocks | 2 | 2/0/0 | 0/0/2 | 2/0/0 |
| diagonal near blocks | 2 | 2/0/0 | 0/0/2 | 2/0/0 |
| single tub | 1 | 1/0/0 | 1/0/0 | 1/0/0 |
| diagonal tubs, supplied two-part inventory | 2 | 0/1/2 | 0/1/2 | 0/1/2 |
| multipart toad plus moving glider | 2 | 2/0/0 | 1/0/1 | 1/0/1 |

## Coverage and unlabelled diagnostics

Across all cases, v2 emits 37 proposals from 478 graph groups, with 239 transient
rejections and 202 abstentions. The ablation emits 31 from 805 groups, with 239
transient rejections and 535 abstentions. V1 emits 26 from 132 initial groups,
with 24 transient rejections and 82 abstentions. These are method-dependent
bookkeeping denominators, including groups that first appear after t=0; they are
not comparable population object counts or independent samples. Correct-match
coverage across the 26 positive scored trajectories is 25/26 for v2, 19/26 for v1
and 20/26 for the ablation. All three emit a false composite on the remaining
two-tub case. Raw per-group dispositions and support hashes are preserved.

All nine diagnostic trajectories emit zero candidates under all three methods.
This is not evidence that they contain no objects. Their unknown labels remain
null, with predictions, group coverage, reasons and failure frames archived:

| Diagnostic | Representative v2 disposition |
|---|---|
| Short-window blinker | Insufficient observed cycles |
| Periodic-edge glider | Four boundary abstentions plus five later groups without t=0 support |
| Overlapping engineered blocks | Complete-group disagreement; later no-t=0 groups excluded |
| Opposed-glider encounter | Union exceeds span bound; no collision-product identity inferred |
| Clutter seed 13 | Boundary/context/recurrence abstentions, transient rejections, later groups excluded |
| Clutter seed 17 | Boundary/context/size/recurrence abstentions, transient rejections, later groups excluded |
| Short-window disconnected toad | Insufficient observed cycles despite successful phase grouping |
| Boundary disconnected toad | Boundary abstention |
| Born transient | Three parent-group transient rejections; one child group explicitly excluded for no t=0 support |

The encounter union being rejected by the size bound does not show that v2
recognized a causal interaction. Likewise, graph-group fragmentation at a grid
edge does not identify separate physical pieces. The born-transient diagnostic
verifies exclusion of later observed supports, not tracking of a new individual.

## Execution, reproduction and checks

One benchmark execution took approximately 0.921 seconds and completed all 38
cases without exceptions. E1–E3 passed in their stated regimes. The retained tub
FP/FNs mean that the narrow expectation flag is not a claim of perfect overall
object recovery. There were no pilot retries, timeouts, test failures, result-
dependent amendments, additional seeds/rules or spontaneous discovery runs.

[The complete JSON](cycle-003-topology-v1.json) includes all raw scientific records
and provenance. SHA-256:
`9bbfeae4ea308c914139f4212d4fe8de15a44782e6ab91ba412644b8bc61a26b`.
The clean execution SHA is `93a1f52479587b1cd5ef13957c200fbddb214bb5`;
Python 3.12.14 and NumPy 2.5.5 were recorded. The protocol hash and every source
hash are included in the output. The environment snapshot is
[cycle-003-requirements.txt](../../experiments/CE-001/cycle-003-requirements.txt).

```bash
git worktree add /tmp/ce003-reproduction 93a1f52479587b1cd5ef13957c200fbddb214bb5
cd /tmp/ce003-reproduction
python -m venv .venv
.venv/bin/python -m pip install -e '.[dev]' numpy==2.5.5 pytest==9.2.0
env PYTHONPATH=src .venv/bin/pytest -q
timeout 300s env PYTHONPATH=src .venv/bin/python -m compositional_emergence.benchmark_topology --output /tmp/ce003-reproduction.json
```

**54 tests passed** in 0.52 seconds. Added checks cover phase recovery and the
edge ablation, previous proximity misses, independently stationary tub parts/
union with the deliberately scored false fusion, reference glider phases,
stationary block-spacing constructions, birth-group exclusion, graph partitions,
the no-shared-coordinate association limit, invalid data/limits, short windows,
panel provenance/counts and non-overwriting evidence. Earlier independent scalar
Life, exhaustive ECA and previous detector tests remain intact.

The independent critic reran the frozen revision, reproduced all scientific
records/provenance except elapsed time, and recomputed exact matches and all
split/count metrics with an independent Counter/multiset procedure. It also
compared all 20 original cycle-002 fixtures, v1 detections and scored evaluations
to their archived records; they are unchanged. Final document audit is tracked
in the governance contribution. Existing output paths are refused, with exclusive
creation protecting evidence from replacement.

## Limits and stop gate

All performance statements are relative to this selected, authored panel and its
explicit inventory convention. Exact fractions disclose denominators; correlated
frames and transformed fixtures do not justify iid population confidence intervals
or significance claims. No robustness guarantee follows beyond the tested phases,
translations, spacings, period/shift bounds, geometry and fixed observation length.
The graph can miss disjoint-coordinate temporal phases and falsely merge spatially
connected or future-contact supports. Neither matching nor adjacency establishes
causal identity, unique decomposition, independent physical components or closure.

The workstream stops at independent review and PR handoff for this approved
cycle. No merge, Stage C, H1–H3 experiment, cycle 004, automatic advancement or
scientific novelty claim is authorized by these results.
