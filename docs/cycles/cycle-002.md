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

| Contribution | Owner | Branch | Deliverables | PR |
|---|---|---|---|---|
| Detector methodology / prior art | Literature Scientist agent | `research/cycle-002-literature` | Verified claim-level primary sources, reproducible search/access log, method comparison, evaluation pitfalls and falsifiers | [#6](https://github.com/sachasimov/compositional-emergence/pull/6) |
| Localized candidate implementation | Simulation Engineer agent | `research/cycle-002-simulation` | Explicit conservative detector, pre-run versioned protocol, meaningful tests, complete engineered benchmark outcomes, baselines and limitations | [#7](https://github.com/sachasimov/compositional-emergence/pull/7) |
| Coordination / critical review | Coordinator and independent Critical Reviewer | `research/cycle-002-governance` | Authorization record, contribution tracking, independent source checks and rerun audit | [#5](https://github.com/sachasimov/compositional-emergence/pull/5) |

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

## Submitted outcomes

The literature submission `f96ffe443fd50b4c76b00246cc93316ad0bf43a6` resolves
the Rupe/Crutchfield and Balduzzi full-text leads, with verified claim locators,
source hashes, evaluation safeguards, and a historical Cook access amendment.
It establishes no novelty or autonomy result and did not inspect implementation
labels or outcomes before its submission.

The implementation submission `a626713e2f75ab20099880d179e11a05d25a789a` archives
the protocol/code frozen at `af942f85f5682e7d2fc330dacf9b53f2351d91e5` and the
single benchmark execution after independent preflight. All 42 tests pass.
Across 14 scored trajectories, the localized method matches 13 of 16 known
objects with no unmatched predictions and three retained false negatives.
Six unlabelled diagnostic trajectories retain every disposition but do not enter
supervised denominators. Whole-grid and occupancy proxy results and their task
mismatch are explicit in the submitted methods report.

The independent [review record](../reviews/cycle-002.md) documents source checks,
the separate-worktree rerun of all 20 cases, an independent matching computation,
and the final disposition. The handoff stops this cycle; these new PRs remain
drafts awaiting human decisions. No third cycle or Stage C run has been started.
