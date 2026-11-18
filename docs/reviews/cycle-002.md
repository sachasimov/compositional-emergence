# Independent critical review — cycle 002

Date: 2026-11-18. Reviewer: Codex agent `/root/critical_review`, separate from
the literature and simulation authors. Scope: CE-001 Stage B localized candidate
validation and methodology literature. No Stage C or H1–H3 experiment is part of
this review. AI review does not authorize merging or another research cycle.

## Submitted revisions and disposition

| Contribution | Revision | Status |
|---|---|---|
| [Governance PR #5](https://github.com/sachasimov/compositional-emergence/pull/5) | `8f6010a6c7ff442a449e7422a02b4188c7268eee` | Scope/authorization and status-document audit complete; no blocking finding |
| [Literature PR #6](https://github.com/sachasimov/compositional-emergence/pull/6) | `f96ffe443fd50b4c76b00246cc93316ad0bf43a6` | Primary-source and methodology audit complete; no blocking finding |
| [Simulation PR #7](https://github.com/sachasimov/compositional-emergence/pull/7) | Submission: `a626713e2f75ab20099880d179e11a05d25a789a`; execution: `af942f85f5682e7d2fc330dacf9b53f2351d91e5` | Preflight, independent reproduction and final archive/methods audit complete; no blocking finding |

## Governance audit

Read the updated operating manual, D-006, historical workstream record, and new
`docs/cycles/cycle-002.md` at the listed governance revision. The update preserves
the earlier cycle as history, records the approved earlier merges, and limits
the continuation to engineered Stage B method validation. Separate contributions,
pre-run protocol versions, independent truth/matching, complete negative and
abstention records, naive baselines, and an independent audit are required.
No third cycle, new-PR merge, Stage C run, or confirmation of H1–H3 is authorized.
No blocking governance finding was identified.

The initial governance revision was `53fee598f379e9b87d4d6dba311740ffb64c9750`.
The subsequent README/RESEARCH status-only update at `8f6010a` was also inspected:
it acknowledges the audited narrow pilot and 29-test baseline while keeping
general detection, H1–H3, and novelty unestablished. It does not expand execution
authorization.

## Pre-execution protocol review

Inspected `experiments/CE-001/cycle-002-localized-v1.md`, `localized.py`, and
`benchmark_localized.py` at `af942f8` before the author ran the benchmark. No
benchmark outcomes were inspected before this preflight and no evaluation-case
selection recommendation was made from results. The reviewer reported no
blocking methodology issue and instructed the author to execute the frozen
panel unchanged, preserving any failure or exception.

The detector consumes a raw Life trajectory and explicit method limits, without
fixture names, ground-truth identities, or expected signatures. Supplied analytic
supports and known periods/displacements define truth. Exact initial-footprint
and recurrence-signature matching assigns each prediction/truth at most once;
different placements of identical patterns retain distinct supports. Duplicate,
wrong-footprint, wrong-period and wrong-displacement predictions cannot hide
behind correct object counts.

Two known segmentation limitations remain scored positives: nearby independent
blocks (two truths) and the disconnected initial toad phase (one truth). Their
abstentions produce false negatives. They are outside the narrowly specified E1
isolation regime but remain in the overall denominators. The six diagnostics
have unavailable object labels and `evaluation: null`; they cannot be silently
counted as clean negatives. Their outputs and component dispositions are retained.
The whole-grid and occupancy baselines have explicit whole-support adapters and
are described as limited candidate-inventory proxies rather than equivalent
segmentation methods.

## Independent simulation reproduction

Created `/workspace/ce-review-simulation-002` as a separate detached worktree at
the frozen execution SHA. Used explicit `PYTHONPATH=src` so imports resolved to
that checkout, with the existing environment supplying dependencies only:

```bash
git worktree add --detach /workspace/ce-review-simulation-002 af942f85f5682e7d2fc330dacf9b53f2351d91e5
cd /workspace/ce-review-simulation-002
env PYTHONPATH=src /workspace/ce-simulation/.venv/bin/python -m pytest -q
timeout 300s env PYTHONPATH=src /workspace/ce-simulation/.venv/bin/python -m compositional_emergence.benchmark_localized --output /tmp/cycle002-independent-review.json
git status --short
```

All **42 tests passed**. The fixed **20-case** benchmark completed with no
exceptions; E1–E3 passed under their stated scope. The reviewer compared complete
`cases`, `metrics`, `expectations`, protocol hash and source/environment/Git
provenance with the author's run. All matched; elapsed wall time was excluded.
Both runs identify clean `af942f8` source. Per-frame hashes, matching assignments,
all predictions, diagnostic records and failure frames therefore agree.

An independent standard-library `collections.Counter` evaluator recomputed
per-case TP/FP/FN from multiset intersections of exact footprint/period/shift
signatures for all three methods on all 14 scored cases. It agreed with the
benchmark's greedy matcher and confirmed unique prediction and truth assignments.
Unknown diagnostics had null evaluations and entered no supervised denominator.

| Combined scored panel: 14 trajectories, 16 truth objects | TP | FP | FN | Precision | Recall | Count MAE |
|---|---:|---:|---:|---:|---:|---:|
| Localized recurrence | 13 | 0 | 3 | 13/13 | 13/16 | 3/14 |
| Whole-grid recurrence proxy | 7 | 1 | 9 | 7/8 | 7/16 | 8/14 |
| Whole-grid occupancy/static proxy | 1 | 12 | 15 | 1/13 | 1/16 | 7/14 |

Development local matching is 8 TP/0 FP/0 FN; held-out matching is 5 TP/0 FP/3 FN.
The three zero-truth controls have no localized false predictions. These are
selected analytic fixtures, not independent population samples or evidence of
performance on spontaneous trajectories.

### Negative evidence, abstentions and ambiguity

- Nearby independent blocks and the alternate-phase toad both receive
  `initial-segmentation-ambiguity`; all three missed truth objects are counted.
  General phase-invariant enumeration therefore fails on this full panel, even
  though the narrower prespecified acceptance expectations pass.
- The short-window blinker abstains for insufficient observed cycles. The seam
  glider produces four initial fragments, all abstained for boundary proximity;
  these are not four physical objects. No periodic unwrapping was validated.
- The engineered opposed-glider tracks abstain at frame 7 due to interaction or
  segmentation change. This is not collision-product or causal-lineage evidence.
- The overlapping-block challenge is rejected as transient, without assigning
  a ground-truth object count. Both clutter cases produce zero accepted
  candidates while retaining all 47 and 39 initial-component dispositions,
  respectively; those include ambiguity, boundary and extinction statuses.
  Zero detections do not establish that clutter is object-free.
- The whole-grid proxy's merged-support false positive and unmatched individual
  truths reflect its explicit adapter/task mismatch. Better scores than these
  proxies do not establish superiority over prior causal-state/filter methods.

The verifier output is `/tmp/cycle002-independent-review.json` with SHA-256
`0d679c77af60ceb4e5593b99b9109a517105ec0f1d903f87b476f2c446178f4e`.
Reproduction uses the same detector and dependencies in a separate checkout,
not an independent detector implementation or a new rule/seed experiment.

## Independent literature checks

Reviewed the submitted methods dossier, query/access log, bibliography changes,
source identity manifest and literature index at `f96ffe44`. The original
cycle-001 ledger remains unchanged. No simulation labels/code/outcomes were used
to construct this literature contribution, and its recommendations are explicitly
prospective rather than a post-result protocol amendment.

Independently searched for the two primary works using the connected web-search
tool and fetched their full primary texts, then checked the dossier's specific
versions and locations. The published Rupe/Crutchfield PDF was also accessible
through UC eScholarship; it is distinct from the 27-page version-pinned preprint
used for the dossier's locators.

| Claims | Independently checked primary text | Disposition |
|---|---|---|
| R1–R2 | [Rupe/Crutchfield arXiv:1801.00515v1](https://arxiv.org/pdf/1801.00515v1), §II B1 Eq. (3), §II B2 | Predictive lightcone equivalence and explicit distinction from direct causal-relationship detection are supported. Finite horizons/speed are method parameters; no finite-data consistency guarantee is inferred. |
| R3–R4 | Same version, §III B definition and §IV C2/Fig. 10 | Localization and persistence require semantic-filter/domain context. Nondomain fluctuations require further structure semantics; occupied-cell recurrence is a different criterion. |
| B1–B2 | [Balduzzi arXiv:1105.0158v2](https://arxiv.org/html/1105.0158v2), Coarse-graining Algorithm Steps 1–3 and Effective information Eq. (4) | Ground/channel/unit construction, fixed context and imposed/uniform inputs are supported. Passive observed transitions alone are not the same interventional quantity. |
| B3–B4 | Same version, Life Fig. 6 and Hopfield “Macroscopic mechanisms depend on the ground” | Selected grainings distinguish gliders/blank regions, and contextual ground affects mechanisms. No general detector score or autonomous-object implication follows. |
| Cook access amendment | [Publisher PDF](https://content.wolfram.com/sites/13/2023/02/15-1-1.pdf), §§1–2 and §2.3 | The newly accessible construction and idealized collision material support the limited access amendment. Neither author nor reviewer claims a full proof audit or spontaneous-frequency result. |

All checks were on 2026-11-18. Independently retrieved the three exact PDF URLs
with Python `urllib.request`, checked the PDF byte signature, and recomputed
length and SHA-256. All matched `source-artifacts-cycle-002.json` exactly:

| Source | Bytes | SHA-256 |
|---|---:|---|
| RC2018 v1 | 3,340,221 | `67306260bd706fac0822348130e29e2ac8cf1220792a31332c09c888c534c71c` |
| B2011 v2 | 425,339 | `ae7953a4621f379751722e43b188f5ad7c29e37dd22a321c1ee608e22906e6f2` |
| Cook publisher PDF | 903,483 | `c9a2885248ae2811c5825c5bcbaa52ca167a7d5300ba88f87ee832b93b293c03` |

The dossier correctly distinguishes geometric candidates, local recurrence,
predictive representations, interventional claims and productive composition.
Its falsifiers, exact matching, negative-opportunity caution, baseline adapters,
cropping/context caveats and unknown-label treatment are sound safeguards for
interpreting this bounded pilot. No stronger prior-method algorithm was
implemented/benchmarked, no source's numerical claims were replicated, and no
novelty or physical-autonomy certification follows from source verification.

## Findings and resolution history

No blocking governance, literature, or simulation-code findings identified.
The preflight did not require changes to the frozen protocol/case table, and no
post-outcome cases or thresholds were substituted. No actionable review finding
or remediation commit was needed in this cycle. The known false negatives are
preserved methodological outcomes, not relabelled as successful enumeration.

Reviewed the final simulation report, experiment index, dependency snapshot and
archived JSON at `a626713`. The report matches the independently reproduced
counts, scope, case-level outcomes and diagnostics. It explicitly notes that the
whole-grid assay recovers the disconnected-phase toad which the local method
misses, and that the current method does not enumerate all supplied objects.

`git diff --exit-code af942f8 a626713 -- src tests experiments/CE-001/cycle-002-localized-v1.md`
confirmed that source, tests and protocol did not change after execution.
`git diff --check` passed on both contribution diffs from the merged baseline.
The final archive identifies the frozen clean execution revision and its
protocol hash matches the committed protocol bytes. Artifact identities:

- Author's archived result SHA-256:
  `00067d460092af59bcae61b880ff4b09c3704bef51b0e7cb842d2716209f3fd2`.
- Frozen protocol SHA-256:
  `2f005c9cb97e6a700c3b48a36993e20586048b5041a4f9e761a9b9aea8a3e46e`.

The governance branch adds this review as a subsequent documentation change;
this reviewer does not claim an independent audit of its own review record.

## Human decision gate

The audit of the submitted contributions is complete. There are no open
blocking findings for accepting the work as a bounded primary-source methods
review and conservative engineered candidate-validation pilot. Source checks
and same-implementation reproduction do not establish general detector validity,
causal autonomy, H1–H3, scientific novelty or productive composition.

The three new PRs remain drafts for human review. Approval of earlier PRs does
not approve these contributions. Do not merge, enable auto-merge, run Stage C,
or start cycle 003 without fresh explicit human approval. This cycle stops here.
