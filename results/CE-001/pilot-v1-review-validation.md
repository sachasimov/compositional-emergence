# Cycle 001 critical-review repairs and validation

This is an in-cycle review repair. The original protocol, run, and methods report
are preserved without changes. The original output JSON SHA-256 remains
`fba40684768e6ea89835a3bc0a479e91bd530d41a2a91c652dba2a1a7ecad7a3`.

The critical reviewer independently reproduced the original test suite and pilot
and identified two actionable issues:

- **CR-S1:** Original P1 described exact known recurrence signatures, but the
  automated acceptance flag compared binary recurrence presence only. The raw
  original outputs do contain all correct signatures. The repair archives
  expected periods/displacements and explicitly checks them. Regression tests
  reject an incorrect period and an incorrect displacement even when the binary
  recurrence prediction is true.
- **CR-S2:** The simulation CLI could overwrite a prior run file. It now rejects
  existing paths and uses exclusive creation to avoid a check/create race. The
  regression test reruns with a different seed into an existing output and
  verifies that the original bytes survive unchanged.

[The amendment](../../experiments/CE-001/pilot-v1-review-amendment-1.md) and repair
implementation were committed at `2d6e5bf` before a single review-validation
execution. [The complete validation JSON](pilot-v1-review-validation.json)
records the full clean execution SHA, source hashes and amendment hash. The
original 19 cases, all inputs, predictions, recurrence outputs and baseline
confusion metrics match the preserved original run. Every exact expected
signature now passes the stronger automated acceptance check. The suite passed
**29 tests** in 0.34 seconds; the review-validation pilot completed without
exceptions. Negative and unlabelled diagnostic outcomes remain unchanged.

Reproduce the repair SHA using the virtual-environment setup in the original
report, then run:

```bash
.venv/bin/pytest -q
.venv/bin/python -m compositional_emergence.benchmark --output /tmp/ce001-review-validation.json
```

The benchmark default uses the amendment; do not relabel the original run as if
it used the stronger automated acceptance check. Compare case inputs, signatures,
exact acceptance flags, metrics and source/protocol hashes. Timing and Git dirty
metadata can differ. No failed pilot runs occurred. Independent re-review is
pending at authorship; no merge, Stage C run or subsequent cycle is authorized.
