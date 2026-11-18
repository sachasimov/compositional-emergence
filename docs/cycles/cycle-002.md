# Cycle 002 — localized candidate validation

Date: 2026-11-18. Baseline: merged cycle-001 contributions at
`18c7beff8f60ff60e28b81db2b9ac1250127e099`. Authorization and interpretation are
recorded in D-006. The integrated baseline passes 29 tests. This document defines
scope and handoff requirements, not the executable scientific protocol; the
implementation workstream freezes its own versioned protocol before execution.

## Question and scope

Can a conservative method identify multiple persistent localized candidates
from unlabelled Life trajectories when the full grid does not recur under one
translation? Specify exactly when segmentation, recurrence, and tracking are
valid, and when the method must reject or abstain. A geometrically detected
candidate is not evidence of autonomy, productive composition, or a physical
individual. This is engineered method validation in CE-001 Stage B.

## Independent workstreams

| Contribution | Owner | Branch | Deliverables |
|---|---|---|---|
| Detector methodology / prior art | Literature Scientist agent | `research/cycle-002-literature` | Verified claim-level primary sources, reproducible search/access log, method comparison, evaluation pitfalls and falsifiers |
| Localized candidate implementation | Simulation Engineer agent | `research/cycle-002-simulation` | Explicit conservative detector, pre-run versioned protocol, meaningful tests, complete engineered benchmark outcomes, baselines and limitations |
| Coordination / critical review | Coordinator and independent Critical Reviewer | `research/cycle-002-governance` | Authorization record, contribution tracking, independent source checks and rerun audit |

Both workstreams start from the same merged baseline in separate worktrees.
Literature recommendations may identify weaknesses but cannot silently alter a
frozen evaluation after its results are known. Preserve any amendment and its
reason, original outcomes, and subsequent recheck. Do not fabricate independence
between authored fixtures or count adjacent frames as independent experiments.

## Acceptance criteria

- Literature checks the actual primary text and version for each substantive
  claim. Unavailable full text remains an explicit limit. Compare local causal
  states and other applicable methods without claiming a geometric method has
  their causal interpretation or certified novelty.
- Freeze the detector definition, observation limits, isolation/interaction
  assumptions, cases and splits, labels/matching rules, metrics, baselines,
  failure handling, and resource/stop limits before running the benchmark.
- Use known persistent fixtures, differently moving separated structures,
  transient/empty controls, transformed held-out controls, and unscored ambiguous
  clutter/overlap/collision/wraparound/short-window challenges as appropriate.
  Define truth independently of the implementation and report count/matching
  errors and abstentions rather than merely whole-trajectory binary presence.
- Archive every case, parameter, initial-state provenance, source/protocol hash,
  revision/environment, exception, false positive/negative, and ambiguity with
  exact commands. Refuse to overwrite prior evidence.
- Include transparent simple baselines, including the existing full-grid assay,
  and explain when comparisons measure different tasks. Preserve poor results;
  a method failing its prespecified expectations is a valid outcome.
- Keep CPU execution below five minutes per bounded benchmark. No paid compute,
  target-structure search, new rule/seed search, or spontaneous discovery run.
- The independent critic audits exact submitted revisions and sources, reruns
  tests and benchmark in a separate worktree/output path, and records findings,
  author responses, rechecks, limitations, and final disposition.

## Handoff and stop gate

Open separate draft PRs against `main`, publish their review records and links,
and stop after this cycle. Approval for the earlier audited PRs does not approve
these new PRs. No merges, auto-merge, third cycle, Stage C, or H1–H3 experiment
without fresh explicit human approval. No validated finding or scientific
novelty is presumed from completion of this work.
