# Critical review process

Every contribution receives an audit by an agent that did not implement it.
The coordinator checks that the reviewer has the submitted revisions and can
inspect the evidence directly. An AI audit supports human review; it does not
replace human merge approval or establish a validated scientific finding.

## Review sequence

1. Freeze the submitted commit and list the protocol/source revisions and output
   paths. Check the diff for unrelated changes and undocumented protocol changes.
2. Audit each cited claim against the primary text and its exact locator.
   Distinguish verified full-text claims, abstract-only evidence, and unresolved
   access gaps. Search for prior overlap and contradictory evidence.
3. Check that hypotheses can fail and that metrics, controls, baselines, stop
   rules, and held-out status were specified before the relevant run. Flag
   post-hoc changes and limits of pilot or engineered validation data.
4. Independently rerun the tests and bounded experiment in a fresh output path.
   Compare deterministic scientific outputs and hashes while accounting for
   expected environment/provenance differences. Check all cases, including
   negatives, errors, ambiguous cases, and zero-denominator metrics.
5. Test plausible failure modes: invalid inputs, boundary wraparound, insufficient
   observation windows, overlapping structures, biased labels, correlated
   observations, leakage, and weak baselines. Identify what the evidence cannot
   establish, including untested H1–H3 claims.
6. Write a dated audit with reviewed commit IDs, commands actually run, outcomes,
   source checks, findings, unresolved risks, and a scoped recommendation.

## Findings and closure

Use `BLOCKER` for incorrect results, fabricated/unverified support for a central
claim, irreproducibility, or violations of the authorized scope. Use `MAJOR` for
material methodological gaps and `MINOR` for nonmaterial clarity issues. Each
finding needs a stable ID, location, evidence, consequence, and concrete remedy.
State explicitly when no blocking findings are found; absence of a finding is
not proof of correctness.

The author addresses findings in commits or documents why a limitation remains.
The reviewer rechecks changed portions and records closure or continuing
objections. Any unresolved blocker prevents a recommendation to accept the
affected claim. Preserve the original finding and response history.

## Human decision gate

Post a concise audit summary on each contribution PR and link the durable review
record. Hand off PRs with all limitations visible. Stop after this approved cycle.
Only explicit human approval authorizes a merge or another research cycle;
passing tests, a favorable agent review, and PR creation do not authorize either.
