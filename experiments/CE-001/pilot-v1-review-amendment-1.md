# CE-001 pilot v1: critical-review amendment 1

Date: 2026-11-18. This is an implementation repair within cycle 001, not a new
research cycle. Freeze this amendment and its implementation before running the
review-validation reproduction. The original [pilot-v1.md](pilot-v1.md), original
execution revision `2722fbb3ee6644958146fb6624c49507e7510fb3`, original results
`results/CE-001/pilot-v1.json`, and original methods remain preserved.

Critical review CR-S1 found that P1 specifies known periods and displacements but
the acceptance flag only checked binary presence of recurrence. All recorded
original signatures were correct on manual inspection; the original automated
flag alone did not establish that stronger assertion. Repair: explicitly archive
expected signatures for all six positive fixtures and compare the observed period
and displacement with them. A wrong signature must fail the entire validation
run even if binary classification remains correct. Negative fixture expectation
is absence of recurrence. Diagnostic cases remain unscored and their outputs
remain archived without reinterpretation.

Critical review CR-S2 found that the Stage A simulation CLI could overwrite prior
output. Repair: refuse existing paths and use exclusive file creation, with a
regression test preserving original bytes during a second attempted run.

All original sampling, controls, 19 fixture inputs, period/shift bounds, baseline
comparisons, metrics, budget and stop conditions remain as specified in pilot v1.
This single reproduction validates the review fixes and compares fixture inputs,
signatures and confusion counts to the preserved original. No tuning, new seeds,
new rules, new cases, spontaneous experiments or follow-on cycle is authorized.
The default benchmark protocol hash now refers to this amendment; the frozen
original protocol remains at the linked path in the same versioned repository.
