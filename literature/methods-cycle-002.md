# Stage B detector methodology review — cycle 002

Date: 2026-11-18. Author: Literature Scientist agent. Base revision:
`18c7beff8f60ff60e28b81db2b9ac1250127e099`. Evidence state: checked literature
and proposed evaluation safeguards, not detector performance or an H1–H3 result.

This bounded review resolves two prior reading leads and one access gap. It is
independent of the implementation workstream: no cycle-002 simulation labels,
thresholds, code, or outcomes were inspected or tuned for this contribution. The original
cycle-001 ledger remains a historical record. The user approved this additional
cycle; further cycles and Stage C remain outside this workstream's authorization.

## Primary evidence and exact scope

**RC2018.** Adam Rupe and James P. Crutchfield, *Local Causal States and Discrete
Coherent Structures*, [arXiv:1801.00515v1](https://arxiv.org/pdf/1801.00515v1),
submitted 2018-01-01; PDF dated 2018-01-03. The
[arXiv record](https://arxiv.org/abs/1801.00515v1) links journal DOI
[10.1063/1.5021130](https://doi.org/10.1063/1.5021130). The journal text was not
compared; page locators below identify the **27-page preprint**, counting from 1.

| Claim ID | Checked locator | Supported content |
|---|---|---|
| R1 | §II B1, Eq. (3) and following discussion, pp. 4–5 | States group past lightcones by their conditional distributions of future lightcones. The authors explicitly distinguish this prediction construction from detecting direct causal relationships. |
| R2 | §II B2, pp. 5–6 | Filtering uses finite past/future horizons and a propagation speed; these are declared implementation parameters. |
| R3 | §III B, definition, pp. 11–12 | Coherent structures require localization relative to a domain and temporal persistence in the filtered field. A raw occupied-cell component is not this definition. |
| R4 | §IV C2, pp. 19–21, Fig. 10 | ECA18 illustrates that nondomain labels alone can include fluctuations; further structure semantics matter. |

Full text at these locators was checked. No estimator, theoretical result, or
numerical example was independently replicated. In particular, no claim of
interventional autonomy or guaranteed finite-data consistency follows here.

**B2011.** David Balduzzi, *Detecting emergent processes in cellular automata with
excess information*, [arXiv:1105.0158v2](https://arxiv.org/html/1105.0158v2),
revised 2011-09-22. [PDF v2](https://arxiv.org/pdf/1105.0158v2) was also retrieved.
Named HTML headings and equation numbers are used rather than guessed journal
pages. The [author's institutional record](https://is.mpg.de/ei/publications/balduzzi2011)
was readable initially but later returned 403; it is unnecessary for the claims.

| Claim ID | Checked locator | Supported content |
|---|---|---|
| B1 | “Coarse-graining”, “Algorithm”, Steps 1–3, Eqs. (2)–(3) | Construction partitions occasions into ground, channel and units, fixes ground outputs, and marginalizes external inputs uniformly. |
| B2 | “Information”, “Effective information”, Eq. (4) and following paragraph | Repertoires use imposed inputs and a uniform input distribution, rather than merely observed transition frequencies. |
| B3 | “Application: Conway's Game of Life”, Fig. 6 and “Excess information detects gliders” | Selected spatial grainings distinguish blank regions and gliders and their motion. |
| B4 | “Application: Hopfield networks”, “Macroscopic mechanisms depend on the ground” | Fixing context changes the coarse-grained mechanism. |

Full text at these locators was checked. The examples do not establish general
detector precision, causal independence under arbitrary coupling, or
compositional productivity. No numerical reproduction was attempted.

**C2004 access amendment.** Matthew Cook, *Universality in Elementary Cellular
Automata*, Complex Systems 15(1), 1–40 (2004). The audit-supplied
[publisher PDF route](https://content.wolfram.com/sites/13/2023/02/15-1-1.pdf)
now works. Spot-checked §§1–2, pp. 1–3, on universality/encoding and §2.3,
pp. 8–9, on idealized glider collisions. This repairs availability, not a full
proof audit or a spontaneous-occurrence result. The cycle-001 failed route is
retained in its historical log.

Downloaded source hashes, lengths, versions and retrieval outcomes are in
[source-artifacts-cycle-002.json](source-artifacts-cycle-002.json); the search
and failure record is [search-cycle-002.md](search-cycle-002.md). None of the
papers is bundled into the repository.

## What Stage B may claim

The following is our proposed measurement contract, informed by R1–R4 and
B1–B4. It is not a claim that these papers prescribe our benchmark.

| Output layer | Evidence required | Permitted interpretation |
|---|---|---|
| Geometric candidate | Declared adjacency, crop, and reference time | A segmented region; no persistence assertion. |
| Local recurrence candidate | Verified finite evolution, comparison region, period/shift bounds and isolation assumptions | A candidate satisfying this particular recurrence assay. |
| Predictive representation | Defined target, ensemble, history, estimator and untouched evaluation data | Predictive sufficiency within tested conditions. |
| Causal or coupling claim | Explicit interventions and counterfactuals with controlled context | Only the measured intervention's effect under its assumptions. |
| Productive composition | Valid identity/event tracking and ancestry plus a product endpoint | A separate research question, beyond this Stage B pilot. |

There is no automatic implication from an earlier row to a later one. For this
cycle a localized candidate assay is useful infrastructure, even if it cannot
support the final research claim. Calling it a “causal-state detector” would
require implementing and validating the predictive-equivalence construction,
not merely giving a recurring connected component that name.

## Actionable implementation and evaluation safeguards

These are prospective requirements for interpreting the independent Stage B
implementation. They do not amend a frozen implementation protocol after seeing
results, and any discrepancy must be recorded as a limitation or later amendment.

1. **Freeze the estimand.** State whether labels identify objects present at a
   reference frame, detections anywhere in a clip, or entire tracks. Publish masks,
   times, and expected counts independently of the detector. A late transient
   becoming recurrent does not retroactively change an initial-frame label.
2. **Make segmentation explicit.** Define 4-/8-neighbor adjacency, toroidal
   connectivity, disconnected assemblies, minimum size, padding, and handling of
   merges/splits. A single connected region can contain interacting structures;
   multiple regions can jointly form one candidate. Preserve these cases as
   ambiguities unless an independent label rule resolves them.
3. **Do not create isolation by cropping.** A crop with imposed empty/periodic
   boundaries evolves a different initial-value problem. Retain the surrounding
   trajectory and declare a causal-margin or isolation test over the full search
   horizon. If the dependency region leaves the recorded data, report censored or
   unsupported status, not a certified object. Clipping escaping live cells can
   manufacture equality. A finite blank halo is not indefinite autonomy.
4. **Retain finite-window blind spots.** A missed period/shift outside the search
   bounds is not evidence of nonexistence. A near-edge object and an object whose
   future encounters wrap the torus need explicit boundary status. Distinguish a
   finite recurrence witness from a longer-horizon interaction assertion.
5. **Freeze any learned representation.** If predictive states are added later,
   declare cone geometry, propagation speed, horizons, sampling ensemble, state
   merging tolerance, minimum support, and unseen-context handling before scoring.
   Fit only on development trajectories; splitting adjacent frames can leak the
   same structures into both sets. Report prediction loss and segmentation
   performance separately.
6. **Keep mechanism and observational baselines distinct.** A method with an
   explicit rule table and intervention distribution receives information a
   passive trajectory filter may lack. Specify access and compute budgets and
   the conversion from each method's output to benchmark instances. Do not rank
   unlike outputs as if their targets were identical.

## Fair baselines and a reproducible scoring contract

For this deliberately narrow pilot, reasonable simple comparators are:

- **No candidates:** exposes class imbalance and undefined precision.
- **Geometric components:** emit all components at the declared reference frame;
  measures the value of the temporal criterion beyond segmentation alone.
- **Local stationarity:** apply the same candidate-generation and boundary rules
  but require unchanged one-step support; isolates oscillation/translation gains.
- **Whole-grid recurrence:** retain the old binary world-level answer as a
  separate endpoint. If evaluated as instances, freeze an adapter that emits one
  whole active-support mask on success. Do not pretend one flag identifies every
  local object.

These are weak method controls. They cannot establish superiority to R/B methods,
which are **not implemented or benchmarked by this review**. A claim about a new
general detector would require stronger applicable prior-method comparisons and
additional data, outside the present approval.

For analytic reference-frame fixtures, our proposed primary matching rule is
exact equality of live-cell masks at that frame, with at most one prediction
matched to each truth instance and vice versa. Count duplicate detections as false
positives and unmatched truths as false negatives. If approximate masks are needed,
freeze the overlap threshold, torus convention and one-to-one matching algorithm
before execution; report that different endpoint separately. A detection-count
match alone can hide both a miss and a spurious detection.

Preserve case-level truth, predictions, matching assignments, TP/FP/FN, and errors.
Report precision and recall with null for zero denominators; a true-negative rate
requires a separately defined population of negative opportunities, not every
unoccupied cell. Include exact fractions, development/held-out splits, per-case
runtime and exclusions. Fixed engineered panels warrant descriptive results, not
iid population intervals. Translations/phases of a fixture are robustness checks,
not independent samples for precision estimates.

Random clutter is not automatically a negative: it can contain valid candidates.
Label such cases unknown or use an independent finite-horizon annotation/oracle
for the declared endpoint. Keep positive, negative, ambiguous, boundary, collision,
short-window, and multi-candidate cases even when the method fails. Store complete
initial states or hashes with construction rules, dependencies, code/protocol
revisions, seeds, and all settings in one rerunnable run index.

## Falsifiers, negative findings, and stop

The following evaluation criteria are proposed checks; they are not observations:

- A claim of exact enumeration on a finite analytic panel fails on any unmatched
  truth or extra prediction under the frozen matching rule.
- A claim of added value over geometry fails on that panel if temporal filtering
  does not reduce the prespecified error relative to component-only output.
- A claim of boundary robustness fails on any declared equivalent translated
  fixture whose output changes after coordinate normalization. Excluded seam cases
  must remain visible and cannot support robustness.
- A claim of general causal autonomy remains unsupported regardless of scores on
  these recurrence criteria. No H1–H3 or compositional endpoint is measured.

The completed literature result is methodological: two previously unresolved
primary works are directly relevant prior art, and their criteria differ from a
geometric recurrence candidate. This is negative evidence against broad novelty
or causal claims from Stage B. Access recovery does not remove the remaining
absence of replicated algorithms, untouched broad datasets, coupling tests, or
composition ancestry. No simulation, rule search, Stage C run, or third research
cycle was executed by this workstream. Independent critique and a PR handoff end
this authorized contribution.
