# CE-001 exact-recurrence assay pilot v1 — frozen supplement

Frozen before the first pilot execution by the code/protocol commit; this does
not replace `protocol.md`. Date: 2026-11-18. Evidence state: protocol until run.

## Scope and falsifiable expectations

This is a small engineered method-validation panel, not a spontaneous discovery
experiment, a general object detector benchmark, or a test of H1–H3. No Stage C
runs or next research cycle are authorized by this protocol.

P1: the assay identifies exact recurrence in the four analytic Life fixtures
(block period 1, blinker period 2, glider period 4 with diagonal displacement,
toad period 2) and excludes four empty/extinguishing fixtures (empty, one cell,
adjacent pair, separated pair). Any mismatch falsifies P1 for this panel.

P2: the same behavior survives an a priori held-out reflected glider, rotated
toad and separated diagonal pair. Any mismatch falsifies P2. These transformations
are a minimal generalization check, not a statistically independent test set or
evidence of performance on spontaneous objects. No fitting or threshold selection
uses these cases. Entire panel and labels are fixed in `benchmark.py` before run.

Alternative baseline: nonempty occupancy is sufficient to distinguish persistent
fixtures from negative controls. Compare confusion counts with this baseline and
a nonempty one-step stationary baseline. The occupancy alternative is rejected
only on this panel if the assay has fewer classification errors. Stationarity
should miss moving/oscillating fixtures; this is an explicitly weak baseline.

## Fixed design

- Rule: Life B3/S23, Moore neighborhood, synchronous periodic 32×32 grid.
- Assay v1: full-grid equality to an initial-state translation, periods 1–12,
  shifts −4…4 on each axis, deterministic tie-breaking in `structures.py`.
- Primary panel: 11 scored fixtures above, each run once. Every initial live-cell
  coordinate and expected binary label is archived. Labels derive from finite
  pattern behavior; they do not assert physical individuality.
- Diagnostic cases, excluded from primary metrics: blinker with period window 1;
  glider with shift bound 0 and period window 4; separated block plus glider;
  glider crossing a boundary; overlapping blocks; opposed gliders directed toward
  each other; clutter initialized with PCG64 seeds 7 and 11, density 0.25.
- Diagnostic annotations are qualitative expectations/limitations, not ground
  truth labels for object identity or evidence that a collision generated a new
  object. Do not tune to observed outcomes. Preserve unexpected outputs.
- Metrics: TP/FP/TN/FN, precision, recall, false-positive rate, accuracy per split
  and combined. Undefined denominators are JSON null. Report exact fractions and
  counts. No population confidence intervals: these are fixed, selected fixtures,
  not an iid random sample. Timing is total wall-clock seconds, descriptive only.
- Budget: CPU only, one complete run, <5 minutes; stop on a primary mismatch or
  exception after recording all cases. Exit nonzero on either. Preserve exception
  text and every other result. No seed/rule searches, retries to improve results,
  or automatic follow-on experiments.

## Reproducibility and gates

Run `python -m compositional_emergence.benchmark --output PATH.json` after tests.
The output includes source hashes, Git revision/dirty state, Python/NumPy versions,
protocol SHA-256, parameters, coordinates, input hashes, every prediction and
exception, metrics, and timing. Archive the result and methods report together.
Runtime duration and Git dirty metadata may differ on reproduction; compare
fixture inputs, predictions, confusion counts and source/protocol hashes.

A passing panel supports implementation checks only. General detector validation,
tracking, object annotations, collision-product lineage, finite-size sensitivity,
uncertainty for sampled trajectories, H2 and Stage C remain pending. Independent
critical review and human approval govern advancement.
