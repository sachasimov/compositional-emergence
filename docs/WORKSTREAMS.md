# Initial research cycle — CE-001 foundation

Historical cycle-001 record. The user subsequently approved merging PRs #2, #4,
and #3; all are merged, with integrated `main` at `18c7bef`. Current authorized
work is [cycle 003](cycles/cycle-003.md), limited to Stage B phase/proximity
validation. Cycle-002 PRs #5–#7 were subsequently approved and merged as well.

Authorization: user request in Codex, 2026-11-18. One cycle with two independent
workstreams is approved. Merge and any subsequent research cycle require
explicit human approval. The coordinating agent prepares the reviewable work;
the human decides whether to accept it. No automatic advancement is authorized.

## Responsibilities and isolation

| Contribution | Owner | Branch | Scope | Pull request |
|---|---|---|---|---|
| Research governance | Coordinating agent | `research/cycle-001-governance` | Operating manual, review process, contribution tracking | [#2](https://github.com/sachasimov/compositional-emergence/pull/2) |
| Literature / novelty | Literature Scientist agent | `research/cycle-001-literature` | Verified primary sources, claim matrix, search log, bounded novelty assessment | [#4](https://github.com/sachasimov/compositional-emergence/pull/4) |
| CE-001 implementation | Simulation Engineer agent | `research/cycle-001-simulation` | Tested simulation, versioned assay protocol, reproducible pilot and complete outcomes | [#3](https://github.com/sachasimov/compositional-emergence/pull/3) |
| Independent critique | Critical Reviewer agent | Review records on governance branch and PR comments | Audit both contributions and independently rerun the bounded pilot | [Audit in #2](https://github.com/sachasimov/compositional-emergence/pull/2) |

The two workstreams begin at the same repository revision and use separate
worktrees and branches. Neither depends on the other's unpublished findings.
The coordinator reconciles contradictions during review, with explicit changes
and evidence rather than treating agreement between agents as validation.
Role names identify AI responsibilities, not human collaborators or GitHub
accounts. Record the actual author and reviewer in each handoff.

## Literature acceptance criteria

- Inspect primary publications or author-hosted originals; verify bibliographic
  metadata and the specific claims used, with section/page locators and URLs.
- Record queries, access dates, inspected sources, excluded or unavailable
  material, and limits of coverage. An unsuccessful search is not proof of novelty.
- Map H1–H3 and candidate contributions to closest prior results, assumptions,
  counterexamples, unresolved overlap, and discriminating falsifiable tests.
- Specify simple competing explanations and baselines. Explicitly retain
  negative novelty findings and mark all proposed gaps as provisional.

## Simulation acceptance criteria

- Test local CA rules and boundaries against independent expected behavior;
  reject invalid states without silently coercing them into valid binary data.
- Version the bounded pilot protocol before execution, including hypothesis,
  controls, cases, metric definitions, baselines, sampling unit, and stop rules.
- Record exact source identity, environment, initial conditions/seeds, parameters,
  and reproduction commands. Preserve every case, error, negative result, and
  ambiguity in compact inspectable outputs.
- Compare the narrow recurrence assay against an explicit simple baseline and
  describe detector blind spots. Do not equate full-grid recurrence with object
  identity or compositional productivity.
- Keep Stage C and confirmatory H2 research pending. Completion of an assay
  benchmark does not approve a new research cycle.

## Pull request tracking

Use separate PRs against `main` for governance and each workstream, preserving
their independent changes. Each PR identifies its owner/role, scope, source
revision, artifacts, verification commands and actual outcomes, negative
evidence, limitations, and independent review record. Use draft status while
human decisions remain outstanding. Do not enable auto-merge.

The coordinator records final PR links and audit dispositions in
`docs/reviews/cycle-001.md`. Track review findings as stable IDs with severity,
evidence, author response, resolution, and remaining human decisions. Source
changes after review invalidate the affected part of the review until rechecked.

## Cycle handoff

Both workstreams completed their bounded initial contributions. The independent
[audit](reviews/cycle-001.md) found and verified repairs for two implementation
issues; no open blocking findings remain for the submitted dossier and assay
pilot. This is not a validation of H1–H3, a general detector, or scientific
novelty. The pilot retains all 19 engineered cases; 29 implementation tests pass.
The literature dossier records substantial prior overlap and primary-text access
limits. At the initial handoff all three contribution PRs were drafts awaiting
human decisions; those decisions and approved merges are recorded in D-006.

This authorized cycle is stopped. No merge, automatic advancement, Stage C run,
or subsequent research cycle was authorized by that initial handoff itself.
The subsequent user approval authorizes only the continuation recorded above.
