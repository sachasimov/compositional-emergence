# Research decision log

## D-001 — Scientific work before orchestration
Use a coordinating researcher, coding executor, and independent critic; add autonomous multi-agent orchestration only after reproducible end-to-end experiments exist.

## D-002 — No built-in goal for complexity
Use fixed rules and documented initial states. Engineered configurations are validation controls, never spontaneous discoveries.

## D-003 — Narrow metrics first
Exact translational recurrence is a sanity test for isolated patterns, not a complete detector of physical individuality.

## D-004 — Protect negative evidence
Record all runs, including null and failed runs. Prefer simple interpretable baselines.

## D-005 — One approved cycle with independent contributions
On 2026-11-18 the user authorized literature/novelty research and CE-001
simulation implementation as independent workstreams, with critical review and
GitHub PR tracking. Separate branches and PRs preserve contribution provenance.
Do not merge PRs, enable auto-merge, or initiate a new research cycle without
explicit human approval. See `WORKSTREAMS.md` and `CRITICAL_REVIEW.md`.

## D-006 — Approved merges and one bounded continuation
On 2026-11-18, after the cycle-001 handoff explicitly left merges and further
cycles awaiting approval, the user replied "do it". The coordinator stated its
interpretation: merge the three reviewed PRs and execute one further bounded
cycle focused on CE-001 detector validation. PRs #2, #4, and #3 were merged with
their audited heads verified and source commits preserved; integrated `main`
at `18c7beff8f60ff60e28b81db2b9ac1250127e099` passes all 29 tests.

Cycle 002 retains independent literature and implementation contributions with
critical review. Its scope is Stage B localized-candidate method validation,
not Stage C discovery or H1–H3 confirmation. New PRs and a third cycle require
fresh approval. See `cycles/cycle-002.md`. Preserve cycle-001 protocols, outputs,
and audit as historical records.

## D-007 — Approved cycle-002 merges and targeted failure analysis
On 2026-11-18, after the cycle-002 handoff left its three new PRs in draft and
stopped pending approval, the user instructed "continue". The coordinator
stated its interpretation: merge reviewed PRs #5, #6, and #7 and execute one
further bounded cycle focused on the three retained detector misses. Audited
heads were checked before merge; original source/protocol commits were retained.
Integrated `main` at `aeed31d4487908029b0107f253f8329a795a78cd` passes 42 tests.

Cycle 003 tests phase/proximity limitations and new errors of any revised
localized method. Prior misses are development regressions, not untouched
validation. Use prespecified extended checks, the previous method on identical
inputs, an appropriate local ablation, independent literature and critical
review. This approval does not cover new PR merges, cycle 004, Stage C, or
H1–H3 experiments. See `cycles/cycle-003.md`.
