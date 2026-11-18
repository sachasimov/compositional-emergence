# CE-001 — Persistent structure detection benchmark

Start with [protocol.md](protocol.md), then inspect the proposed [manifest template](manifest.example.json).

**Current status:** Stage A simulator and tests exist; general Stage B detector validation and Stage C remain pending. A limited Stage B assay pilot is documented below. Do not interpret baseline tests as a result about emergence or composition.

## Cycle 001 implementation and assay pilot

Stage A now records full initial/final states, hashes, PCG64 initialization,
dependency versions, source hashes and Git provenance. Numeric input validation
rejects values before lossy conversion. See [pilot-v1.md](pilot-v1.md) for the
frozen engineered recurrence-assay supplement and
[the recorded methods/results](../../results/CE-001/pilot-v1-report.md).

The supplement executes a limited Stage B assay pilot only: general object
detection, event tracking and Stage C remain pending. It does not supersede the
original draft protocol or establish any emergence/composition hypothesis.

The independent critical review produced
[amendment 1](pilot-v1-review-amendment-1.md) for exact signature acceptance and
run-file preservation. The original run remains archived; see
[review validation](../../results/CE-001/pilot-v1-review-validation.md) for the
separate repair execution and unchanged negative/diagnostic results.

## Cycle 002 localized candidates

The [frozen localized-candidate protocol](cycle-002-localized-v1.md) defines a
conservative window-start assay that can distinguish separated structures with
different motion. The [complete results and limitations](../../results/CE-001/cycle-002-localized-v1-report.md)
retain three scored false negatives and six unlabelled diagnostic trajectories.
This advances bounded Stage B methodology; general object identity, births,
collision-product tracking, Stage C and H1–H3 remain untested.
