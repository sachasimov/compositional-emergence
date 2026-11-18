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
