# Independent critical review — cycle 003

Date: 2026-11-18. Reviewer: Codex agent `/root/critical_review`, independent of
the literature and simulation authors. Scope: bounded CE-001 Stage B development
on localized-candidate phase/topology limitations and associated methodology.
No Stage C, H1–H3 experiment, fourth cycle, or new-PR merge is authorized by this
audit. The coordinator records the human authorization separately.

## Submitted revisions and disposition

| Contribution | Submitted revision | Status |
|---|---|---|
| [Governance PR #8](https://github.com/sachasimov/compositional-emergence/pull/8) | `7a95190bae30028ae17a3d7b4449ab1b3443c142` | Governance audit complete; no blocking finding |
| [Literature PR #9](https://github.com/sachasimov/compositional-emergence/pull/9) | `224d552d5b3f6cd9324998a16a20223921e3bb0b` | Primary-source/methodology audit complete; no blocking finding |
| [Simulation PR #10](https://github.com/sachasimov/compositional-emergence/pull/10) | Submitted: `de7a6d3bd2636c69703ff62c6b2e6bb37e39f2d2`; execution: `93a1f52479587b1cd5ef13957c200fbddb214bb5` | Preflight, independent reproduction and final archive/methods audit complete; no blocking finding |

## Pre-execution review

Reviewed the committed protocol, `localized_v2.py`, `benchmark_topology.py`, and
tests at `93a1f5` before the benchmark ran. No benchmark outcomes were inspected
before preflight. The reviewer reported no blocking methodology issue and
instructed execution of the frozen panel unchanged, preserving any failed
expectation or exception.

The detector receives raw Life trajectories and numerical limits, without
fixture IDs, labels, pattern dictionaries or expected signatures. It groups
eight-connected spatial components by shared live coordinates in adjacent
frames. The graph partitions all observed components; candidate proposals cannot
overlap at a frame. Groups without initial support explicitly abstain rather
than becoming newly tracked objects. Whole-group support, not a favorable subset,
must equal isolated initial-support evolution at every observed frame.

`git diff --exit-code` against the merged baseline confirmed `localized.py`,
`benchmark_localized.py`, `automata.py` and `structures.py` unchanged. The old v1
detector is run directly on the same trajectories and scorer. The ablation uses
the same v2 code, changing only retention of temporal edges: both transition
endpoints must have degree one. All validation, recurrence, bounds and scoring
are otherwise shared. It tests this edge policy, not all possible phase trackers.

Every previous scored case, including formerly held-out transformations, is now
a development regression. Prospective authored cases and their analytic supports
are frozen before results; these are not blinded or statistically independent
validation. One-to-one initial-footprint/least-period/displacement matching is
retained. The two-tub challenge is excluded only from narrow E2 acceptance and
remains scored in every full-panel denominator as a conventional two-object
decomposition. No diagnostic unknown labels enter supervised denominators.

Geometric temporal association is not causal identity. The protocol explicitly
discloses false fusion, observation-window dependence, boundary restrictions,
and failure on persistent motions lacking shared coordinates in consecutive
frames. No additional cases were added by the reviewer after freeze.

## Independent simulation reproduction

Used a fresh detached worktree and explicit imports from its `src`, reusing the
existing virtual environment for dependencies only:

```bash
git worktree add --detach /workspace/ce-review-simulation-003 93a1f52479587b1cd5ef13957c200fbddb214bb5
cd /workspace/ce-review-simulation-003
env PYTHONPATH=src /workspace/ce-simulation/.venv/bin/python -m pytest -q
timeout 300s env PYTHONPATH=src /workspace/ce-simulation/.venv/bin/python -m compositional_emergence.benchmark_topology --output /tmp/cycle003-independent-review.json
git status --short
```

All **54 tests passed** and the **38-case** benchmark completed without
exceptions. The author's and reviewer's complete case records, metrics,
expectations, source/environment/Git provenance and protocol hash matched.
Elapsed timing was excluded. Both executions identify clean `93a1f5` source.
Narrow prespecified E1–E3 expectations passed; this does not mean full-panel
perfect recovery.

The reviewer independently recomputed exact per-case TP/FP/FN using
`collections.Counter` multiset intersections of footprint/period/displacement
signatures, then checked unique prediction/truth match assignments and aggregate
split counts/count MAE for all three methods. All agreed. Nine diagnostic
evaluations were null and entered no supervised denominator.

Also compared all 20 original cycle-002 cases with the preserved original JSON:
coordinates, truth, horizons and every trajectory-frame hash were identical.
The v1 detections, predictions and matching evaluations were also identical.
All 14 old scored cases are explicitly marked development regressions.

| Full scored panel: 29 trajectories, 38 supplied objects | TP | FP | FN | Precision | Recall | Count MAE |
|---|---:|---:|---:|---:|---:|---:|
| v2 overlap union | 36 | 1 | 2 | 36/37 | 36/38 | 1/29 |
| Previous localized v1 | 25 | 1 | 13 | 25/26 | 25/38 | 12/29 |
| One-to-one overlap ablation | 30 | 1 | 8 | 30/31 | 30/38 | 7/29 |

Development v2 matching is 16 TP/0 FP/0 FN; prospective-fixed matching is
20 TP/1 FP/2 FN. The previous method has 13/0/3 and 12/1/10 respectively; the
ablation has 13/0/3 and 17/1/5. All three zero-truth cases produce no false
prediction. These are selected correlated fixture families, not population
precision/recall estimates or evidence of superiority over prior research.

### Retained losses, ambiguity and coverage

- The two nearby blocks and disconnected toad phase are recovered by v2 with
  exact masks/signatures. These repair known development failures; they cannot
  be called untouched generalization.
- Every method emits one recurrent composite for the supplied two-tub
  decomposition. It is an unmatched prediction (FP) and misses both supplied
  supports (2 FNs). Scalar reference checks establish that each tub and the
  union are stationary. The label is an explicit operational convention, not
  a uniquely correct physical partition. This failure remains in full metrics.
- The one-to-one ablation recovers nearby separate blocks but misses six
  additional supplied objects relative to v2. This supports a narrow benefit
  of split/merge association on these phase fixtures; it does not identify a
  universal tracking rule.
- All nine diagnostics produce zero candidates while preserving full group
  dispositions. The born-transient case records three extinct initial groups
  and one `no-window-start-support` group. It does not infer a new individual's
  birth or identity. Clutter/overlap/encounter/seam cases remain unlabelled.
- Across the full fixed panel, v2 records 478 graph groups: 37 accepted, 239
  rejected transient and 202 abstained. V1 records 132 tracks (26/24/82), and
  the ablation 805 groups (31/239/535). These grouping units differ across
  methods and are not comparable physical-event denominators. Complete records,
  rather than a selective subset of accepted groups, underpin the reported
  scores. V2 emits candidates in 26 of 38 trajectories, including the fusion
  error; abstention coverage alone does not establish correctness.

The independent result is `/tmp/cycle003-independent-review.json`, SHA-256
`e35047c72082a2e16302b3a025d4181dac39905c560e7f93606920f76cd15dad`.
Reproduction uses the same implementation/dependencies in another checkout and
an independent scorer; it is not an independent detector implementation or
additional scientific rule/seed experiment.

## Governance audit

Inspected the complete governance diff from merged baseline
`aeed31d4487908029b0107f253f8329a795a78cd` to `7a95190`. It records the user's
approved earlier merges and one targeted continuation, keeps historical
protocols/results/reviews intact, and requires same-input previous-method and
local-ablation comparisons. Old misses remain development regressions. New
contribution merges, cycle 004, Stage C and H1–H3 remain explicitly gated. No
blocking governance finding was identified.

## Independent primary-source review

Reviewed the submitted literature memo, exact-query/access log, source-artifact
manifest, and index at `224d552d`. It distinguishes type, instance, phase,
representation and temporal identity, with explicit nonunique-decomposition
examples. The old block/toad misses are known regressions. The author did not
inspect cycle-003 implementation settings, new labels or outputs to prepare the
memo. Its proposed symmetry criteria, spacetime-union reasoning and hypothetical
nonadditivity diagnostic are identified as methodological reasoning, not source
results or newly executed experiments.

On 2026-11-18 the reviewer independently downloaded the three exact primary PDF
URLs using Python `urllib.request`, checked PDF signatures, and recomputed lengths
and SHA-256 values. All matched the committed manifest. Local
`pdftotext -layout` extraction and targeted passage reads checked the following:

| Claims | Primary location independently checked | Outcome |
|---|---|---|
| HC1 | [Hanson/Crutchfield published PDF](https://csc.ucdavis.edu/~cmg/papers/ECA54.pdf), §4.2, printed pp. 175–176 | Filter synchronization and phase/context-dependent domain/defect recognition are supported. |
| HC2–HC3 | Same PDF, §5.1, printed pp. 179–180 | Explicit temporal phases, particle/subparticle interpretations, bounded domain context, deferred disambiguation and all-phase signatures are supported. These are ECA54 constructions, not a Life detector or unique physical partition. |
| HC4 | Same PDF, §5.2, printed pp. 180–181, Table 1/Fig. 9 | Collisions include spatial/temporal shifts and produced or persistent particles; the memo does not equate geometric proximity with those events. |
| S1–S2 | [Shalizi et al. arXiv:nlin/0508001v1](https://arxiv.org/pdf/nlin/0508001v1), §§II A, III and IV C | Perturbation-based sensitivity and predictive-state complexity are distinct; filters rank structural features differently. The preprint is not asserted identical to final journal text. |
| R1–R3 | [Rupe/Crutchfield arXiv:1801.00515v1](https://arxiv.org/pdf/1801.00515v1), §§II B1, III B and IV C2, Figs. 9–10 | Predictive equivalence is distinguished from direct causal inference; domain-relative semantics and finite-lightcone/representation artifacts are explicit. |

Verified source identities:

| Source | Bytes | SHA-256 |
|---|---:|---|
| HC1997 | 4,218,828 | `6c7765a9d9a78be8d653e97c8907cd03632be8ab2cc6ceb1430d0746ed067814` |
| S2006 v1 | 1,723,342 | `83f41119770420b6c2c27f00a174149f0e77b9bd0dbee58db5e512ad975c7456` |
| RC2018 v1 | 3,340,221 | `67306260bd706fac0822348130e29e2ac8cf1220792a31332c09c888c534c71c` |

No numerical source algorithm, theorem, universal invariance or physical
individuality claim was independently established. The literature contribution
has no blocking finding for its bounded methodology purpose. It does not
certify the revised detector, a causal interpretation, or scientific novelty.

## Findings and resolution history

No blocking governance, literature or implementation findings were identified.
Preflight required no protocol/case changes. No post-result tuning or repair
amendment was required; the deliberately scored tub fusion remains a documented
negative methodological result, not relabelled success.

Final simulation report, experiment index, dependency snapshot and JSON archive
at `de7a6d3` were inspected. Their case/split metrics, coverage, diagnostics and
scope statements agree with the independent reproduction. The report explicitly
states whole-window/offline association, zero-coordinate-overlap limitations and
the conventional, nonunique decomposition endpoint. It does not present repaired
development cases as untouched validation or claim physical identity.

`git diff --exit-code` confirmed source, tests and protocol unchanged from the
independently rerun `93a1f5`. `git diff --check` passed on both workstream diffs.
Recorded source SHA-256 values and protocol hash match the final files. Prior
cycle-001/002 frozen protocols and result JSON files were compared with merged
baseline bytes and remain unchanged. Artifact identities:

- Author result SHA-256:
  `9bbfeae4ea308c914139f4212d4fe8de15a44782e6ab91ba412644b8bc61a26b`.
- Frozen cycle-003 protocol SHA-256:
  `0c5e98a807364994a286809abf1ff9ab1bd79c4d0b3d6a11537798d153adbc21`.

This audit record is a subsequent governance documentation change. The reviewer
does not claim an independent audit of its own record.

## Human decision gate

The audit of the submitted contributions is complete, with no open blocking
findings for consideration as a bounded literature/methodology memo and revised
engineered geometric-candidate assay. The false composite and two missed supplied
supports remain material limitations. Reproducing this code and inspecting source
claims do not validate general object detection, physical individuality, causal
autonomy, H1–H3, productive composition or scientific novelty.

The new PRs remain drafts. Earlier approval does not authorize merging these
contributions. No merge, auto-merge, cycle 004, Stage C or H1–H3 experiment without
fresh explicit human approval. The current cycle stops at this handoff.
