# Cycle 003 — phase and proximity limitations

Date: 2026-11-18. Baseline: `aeed31d4487908029b0107f253f8329a795a78cd`,
the approved merged cycle-002 contributions, with 42 tests passing. The user's
"continue" approval and the coordinator's stated interpretation are recorded
in D-007. This is one bounded engineered CE-001 Stage B cycle, not Stage C or
an H1–H3 experiment. The executable benchmark protocol is frozen separately
before execution by the implementation workstream.

## Question

Can a revised raw-trajectory geometric method recover nearby independent blocks
and the disconnected toad phase without creating unsupported candidates or
hiding interaction, boundary, and short-window errors? Fixing those known cases
alone cannot establish generalization: they are development regressions after
cycle-002 observations. Prespecify additional phase, translation, and spacing
checks and disclose how the cases were authored.

## Independent contributions

| Workstream | Owner | Branch | Deliverables |
|---|---|---|---|
| Phase, identity, and segmentation methodology | Literature Scientist agent | `research/cycle-003-literature` | Verified primary claim locators, methodological distinctions, falsifiable invariance criteria, baseline/ablation guidance, bounded search and negative findings |
| Revised localized candidate method | Simulation Engineer agent | `research/cycle-003-simulation` | Explicit general geometric algorithm, frozen extended evaluation, same-input previous-method comparison and local ablation, tests and complete outcome archive |
| Coordination and independent critique | Coordinator and Critical Reviewer | `research/cycle-003-governance` | Authorization/status, contribution PR tracking, preflight, independent source checks and benchmark reproduction, findings and handoff |

The two workstreams use separate branches from the same merged baseline.
Literature must not tune the implementation's cases or claims from its outcomes.
The critic audits a committed protocol before benchmark execution, then audits
the final submissions and independently recomputes matching and metrics.

## Scientific acceptance requirements

- Preserve cycle-001/002 source identities, protocols, outputs and reviews.
  Version the revised method so the old method remains an inspectable baseline.
- Specify segmentation, temporal association, recurrence, localization and
  abstention rules without pattern names, fixture IDs, or truth input. Geometric
  adjacency is not proof of causal influence or physical identity.
- Freeze prospective cases/splits, independently derived truth footprints and
  least-period/displacement signatures, matching rules, metrics, failure handling,
  resource limits and stop criteria before the single benchmark run.
- Keep old failures as development regressions. Add prespecified phase,
  translation and spacing checks; document that authored transformations are
  robustness checks, not independent population samples or blinded testing.
- Evaluate the previous localized method on exactly the same inputs and include
  a clearly adapted local segmentation-only or stationary ablation. Define output
  adapters and access budgets. Do not infer superiority over unimplemented prior
  methods or conflate object counts with correct identities.
- Match predictions to truth one-to-one by frozen footprints/signatures. Report
  all TP/FP/FN, duplicate/merge/split errors, count errors and abstentions, including
  regression failures and newly introduced false positives. Unknown diagnostics
  remain outside supervised denominators, with raw predictions retained.
- Preserve boundary, encounter, overlap, short-window and clutter challenges.
  Any unresolved object labels are explicit, never silently converted to negatives.
- Record exact source/protocol/environment identities, initial conditions,
  every case/error, trajectory hashes, execution commands and elapsed time.
  Refuse prior output paths. Limit the fixed benchmark to five CPU minutes with
  no paid compute, rule/seed search, or target-structure optimization.
- Treat poor performance or failed expectations as valid documented results.
  Any review repair requires an explicit amendment and preserved original run.
  Independently rerun tests and the benchmark in a separate worktree/output,
  compare scientific outcomes and hashes, and audit claim-level primary sources.

## Handoff and stop

Open separate draft PRs, record exact revisions, evidence, negative results,
independent audit and unresolved limitations, then stop. Approval of the earlier
PRs does not authorize merging these new contributions. No auto-merge, cycle 004,
Stage C, or H1–H3 experiment without fresh explicit human approval. A finite
engineered panel does not certify general objects, autonomy, composition or
scientific novelty.
