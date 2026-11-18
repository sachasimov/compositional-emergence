# CE-001 cycle 001: simulation checks and recurrence-assay pilot

Evidence state: reproducible implementation checks and engineered assay
observations; independent audit pending. No H1–H3 or novelty claim is supported
by this pilot. No spontaneous-discovery experiment or new research cycle ran.

## Methods and provenance

The initial implementation and supplement protocol were committed before running
the pilot at `2722fbb3ee6644958146fb6624c49507e7510fb3`. The pilot manifest
[pilot-v1.json](pilot-v1.json) records that clean revision, SHA-256 hashes of every
Python source file and the protocol, Python/NumPy versions, all 19 initial states
as live-cell coordinates, parameters, predictions, exceptions and elapsed time.
Rule B3/S23, periodic 32×32 grids, period window 12 and shift bound 4 were used
except for the two explicitly restricted diagnostics. No results were discarded
and no threshold or fixture changed after observing the results.

The 11 scored fixtures have analytic labels: six recurrent patterns and five
empty/extinguishing states. Eight diagnostic fixtures remain unlabelled and are
excluded from classification metrics. The split named `held-out` means only that
the three specified transformations were not used for tuning; the implementation
author knew their labels before execution. This is not an independent test set.

The simulator also records full initial/final arrays, their byte hashes, explicit
PCG64 generator identity, parameters, source hashes and Git dirty status. This
allows state replay even if random-generator behavior changes across versions.
Invalid fractional, overflowing, negative, nonnumeric and nonfinite cell values
are rejected before conversion to uint8; the prior implementation silently
truncated some of these values.

## Results

| Classifier | TP | FP | TN | FN | Precision | Recall | False-positive rate | Accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Exact recurrence assay | 6 | 0 | 5 | 0 | 6/6 | 6/6 | 0/5 | 11/11 |
| Nonempty occupancy | 6 | 4 | 1 | 0 | 6/10 | 6/6 | 4/5 | 7/11 |
| Nonempty one-step stationarity | 1 | 0 | 5 | 5 | 1/1 | 1/6 | 0/5 | 6/11 |

P1 and P2 fixture expectations passed: block period 1, blinker/toad period 2,
glider period 4 with displacement (1,1), reflected glider period 4 with (1,-1),
and rotated toad period 2. Empty, single-cell, adjacent-pair, separated-pair and
diagonal-pair initial states had no recurrence in the prespecified window.
Development and held-out confusion counts are retained separately in the JSON.

The occupancy alternative made four more classification errors on this panel;
this demonstrates that occupancy alone fails on selected transient controls.
The stationarity baseline missed five oscillating/moving positives. Both are
deliberately simple baselines, and neither comparison estimates performance on
unseen spontaneous objects. No population confidence interval is appropriate
for this fixed, selected panel; exact fractions disclose the small denominators.

## Negative and ambiguous diagnostic outcomes

| Diagnostic | Assay output | Interpretation limited to this assay |
|---|---|---|
| Blinker, period window 1 | No recurrence | Known oscillator missed by insufficient temporal window |
| Glider, shift bound 0, period window 4 | No recurrence | Known spaceship missed without spatial matching |
| Separated block and glider | No recurrence | A single global translation cannot model distinct local objects |
| Glider crossing periodic edge | Period 4, displacement (1,1) | Wraparound recurrence does not establish free-space identity |
| Overlapping blocks | No recurrence | Engineered overlapping shapes lack independent object labels |
| Opposed gliders | No recurrence | No collision identity or product lineage is inferred |
| Clutter, PCG64 seed 7 | No recurrence | Unlabelled finite sample; not certified object-free |
| Clutter, PCG64 seed 11 | No recurrence | Unlabelled finite sample; not certified object-free |

All 19 cases completed without exceptions in approximately 0.14 seconds of total
wall-clock time. This descriptive runtime is machine-specific and does not
substitute for a scaling study. There were no failed pilot executions. The first
environment check found pytest absent; project dependencies were then installed
in the local virtual environment before any checks ran.

## Reproduction and verification

From the repository root, reproduce the exact execution revision in a separate
worktree; copy the pinned dependency list from this results commit if needed.
`requirements-pilot-v1.txt` records installed package versions. The editable
project entry in that list identifies the original Git revision and worktree;
install this project with `pip install -e '.[dev]'` in the reproduction checkout
instead of reusing that entry. Python 3.12.14 and NumPy 2.5.5 were recorded in
the pilot itself.

```bash
git worktree add /tmp/ce001-reproduction 2722fbb3ee6644958146fb6624c49507e7510fb3
cd /tmp/ce001-reproduction
python -m venv .venv
.venv/bin/python -m pip install -e '.[dev]' numpy==2.5.5 pytest==9.2.0
.venv/bin/pytest -q
.venv/bin/python -m compositional_emergence.benchmark --output /tmp/ce001-pilot-reproduction.json
```

The original suite passed **26 tests** in 0.28 seconds. Tests include every
neighborhood for all 256 ECA rules, independent scalar Life updates on multiple
toroidal shapes, unchanged inputs, invalid-value rejection, known pattern
recurrences, recurrence-limit rejection, and full-state/hash replay of Life/ECA
CLI outputs. These checks validate implementation behavior, not original science.

Compare case IDs, coordinates and hashes, recurrence outputs, baseline
predictions, fixture expectations and confusion counts; timing and Git dirty
metadata can differ. The benchmark refuses to overwrite existing output files.

## Remaining limitations and approval boundary

The detector compares entire grids to their initial states. It does not segment
objects, recover structures born after initialization, distinguish multiple
independently moving objects, track collisions, or measure composition. No
finite-size sweep, statistical trajectory study, annotation study or robustness
under coupling was performed. The controlled fixtures deliberately favor a
recurrence assay and cannot establish general precision/recall for object
detection. General Stage B validation and Stage C remain pending. The current
cycle stops at critical review and human decision; no merge or subsequent
research cycle is authorized here.
