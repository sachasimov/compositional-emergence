# Phase, segmentation, and identity — cycle 003

Date: 2026-11-18. Author: Literature Scientist agent. Base:
`aeed31d4487908029b0107f253f8329a795a78cd`. Scope: the approved bounded CE-001
Stage B cycle in `docs/cycles/cycle-003.md` on the coordinating branch. This is
literature verification and a methodology memo, not a simulation report.

The nearby-block and disconnected-toad misses disclosed in the cycle-002 handoff
motivate the question. They are known development regressions, not untouched
tests. No cycle-003 implementation code, fixture labels, parameters, or outcomes
were inspected to prepare this memo. Earlier literature and evidence files are
preserved. No algorithm replication or H1–H3 experiment was run here.

## Checked primary text

These three existing references suffice for the targeted review; no new novelty
survey or bibliography expansion is claimed. Page locators identify the retrieved
PDF, counting its first page as 1, unless explicitly called printed pages.
The [artifact manifest](source-artifacts-cycle-003.json) pins bytes, URLs and
versions; the [search log](search-cycle-003.md) records procedure and limits.

**HC1997:** James E. Hanson and James P. Crutchfield, *Computational mechanics of
cellular automata: An example*, Physica D 103, 169–189 (1997),
[author-hosted published PDF](https://csc.ucdavis.edu/~cmg/papers/ECA54.pdf),
[DOI](https://doi.org/10.1016/S0167-2789(96)00259-X).

| ID | Exact locator | Checked content |
|---|---|---|
| HC1 | §4.2, printed pp. 175–176 / PDF pp. 7–8, Fig. 5 | Domain filtering synchronizes to the underlying pattern and then classifies domain/defect sites. |
| HC2 | §5.1, printed p. 179 / PDF p. 11, Fig. 8 | Particle signatures have temporal phases. The text permits interpreting a particle as interacting subparticles that also count as particles in isolation. |
| HC3 | §5.1, printed p. 180 / PDF p. 12 | The particle filter includes strings from all phases; bounded domain context and deferred classification disambiguate signatures. |
| HC4 | §5.2, printed pp. 180–181 / PDF pp. 12–13, Table 1 / Fig. 9 | Collision descriptions include spatial and temporal shifts, as well as persistent or produced particles. |

These are ECA54 results and constructions. They do not supply a Life detector or
certify a unique physical decomposition. No numerical findings were reproduced.

**S2006:** Cosma Rohilla Shalizi, Robert Haslinger, Jean-Baptiste Rouquier,
Kristina Lisa Klinkner and Cristopher Moore, *Automatic Filters for the Detection
of Coherent Structure in Spatiotemporal Systems*,
[arXiv:nlin/0508001v1](https://arxiv.org/pdf/nlin/0508001v1), submitted 2005-07-29;
related journal [DOI](https://doi.org/10.1103/PhysRevE.73.036104) (2006).

| ID | Exact locator | Checked content |
|---|---|---|
| S1 | §II A, PDF pp. 3–4; §III, PDF pp. 5–9 | Sensitivity uses perturbations; local statistical complexity uses predictive-state information. These are different constructions. |
| S2 | §IV C, PDF pp. 11–12, Figs. 9–12 | Sensitivity, complexity and free-energy filters emphasize different structural features in cyclic CA. |

Final journal text was not compared. The paper's terminology for autonomous
objects does not make a proximity cluster an intervention-tested object.

**RC2018:** Adam Rupe and James P. Crutchfield, *Local Causal States and Discrete
Coherent Structures*, [arXiv:1801.00515v1](https://arxiv.org/pdf/1801.00515v1),
submitted 2018-01-01; printed draft date 2018-01-03. Related journal
[DOI](https://doi.org/10.1063/1.5021130). Only this preprint was re-inspected.

| ID | Exact locator | Checked content |
|---|---|---|
| R1 | §II B1, Eq. (3) discussion, PDF p. 5 | Predictive lightcone equivalence is explicitly distinguished from detecting direct causal relationships. |
| R2 | §III B, PDF pp. 11–12 | Coherent structures require domain-relative locality and temporal persistence in the filtered representation. |
| R3 | §IV C2, PDF pp. 19–21, Figs. 9–10 | ECA18 comparisons expose representation-dependent structure extents and finite-lightcone artifacts; growth constraints help reconcile descriptions. |

No theorem, estimator consistency result, or benchmark was independently
replicated. Prediction, geometric localization and intervention are distinct
evidence requirements. None of these sources licenses an autonomy or composition
claim from a correct geometric footprint alone.

## Our methodological interpretation

The remaining sections are our proposed measurement contract and reasoning,
informed by the checked sources. They are not attributed results of those papers
and do not silently amend the independent implementation's frozen protocol.

### Type, instance, phase, and representation

A **type** may be an orbit of masks under declared phase and spatial shifts.
An **instance** also has a place, reference time and trajectory. Two instances of
the same type must not collapse into one detection after canonicalization.
Conversely, different phases of one isolated recurrent pattern should not become
different types solely because their connected components change.

Canonical type equality does not certify an enduring individual. A translated
copy appearing later can match the type without establishing an identity link.
Record the actual masks and temporal association separately from normalized
type signatures, candidate ordering, and administrative IDs. Multi-solution
canonical anchors or torus displacements need an explicit equivalence/tie rule;
an arbitrary representative is not evidence of a unique motion history.

Domain connectivity in an inferred automaton, connectedness of occupied cells,
and a causal dependency are different relations. Changing the neighborhood or
grouping radius changes a geometric partition; that operation does not by itself
discover or destroy physical individuals. HC2–HC3 provide relevant prior art for
phase-aware recognition, not a prescription for the correct Life partition.

### Proximity, temporal association, and interaction

Distance-based links are candidate proposals. Overlap between possible influence
regions indicates an opportunity, not an observed effect. A persistent proximity
group or an apparent continuation between frames is not a causal interaction
witness. A method can conservatively abstain near other activity, but must report
that as a method restriction rather than calling every excluded pair interacting.

A possible **future**, explicitly model-dependent diagnostic is to compare joint
evolution of two disjoint supports with the union of their separate evolutions
on the same quiescent background, rule, topology and horizon. A difference is an
operational nonadditivity witness for those chosen interventions and partition.
Equality over a finite horizon does not prove independence forever, and deletion
changes context. This diagnostic has not been executed here and is not an H2 test
or an automatic attribution of unique causal ancestry.

### Nonunique decompositions

Recurrence alone cannot select a preferred granularity. As a simple analytic
illustration, two sufficiently separated stationary Life blocks and their union
are all stationary. Describing the configuration as two recurring candidates or
one compound recurring candidate depends on an added convention. This is
reasoning from the declared rule, not a new numerical observation or certified
general theorem. A disconnected phase can similarly make occupied-cell
connectedness an unreliable surrogate for a chosen recurrent type.

HC2 contains a closer published particle/subparticle example. That does not imply
that every compound should be split, every disconnected mask grouped, or a
minimal-support partition is physically correct. Prefer an explicit operational
target: a declared collection of reference masks and signatures, or a prespecified
set of admissible decompositions for genuinely ambiguous diagnostics. Keep
hierarchical candidates visible separately from the scored instance partition.
Do not relabel a merge or split as acceptable only after inspecting predictions.

## Falsifiable invariance criteria

These are proposed criteria for declared admissible isolated recurrent cases.
They are not new experimental results or a proof of universal invariance.

1. **Spatial equivariance.** For a translated input, returned instance masks should
   translate by the same amount while type, least-period/displacement convention,
   and multiplicity remain consistent. Formally, compare unordered scientific
   records in `D(T_a X)` and `T_a D(X)`, ignoring administrative order and timing.
   One unmatched record or changed scientific status falsifies a claimed exact
   relation on that declared test set. A seam-excluding method can claim only
   its restricted admissible-domain behavior; seam failures remain reported.
2. **Phase consistency.** Starting from each prespecified phase of an isolated
   recurrent fixture should recover the same type and count, with the correct
   phase-specific footprint and motion signature. Advance the full fixture and
   context consistently; keep the same usable observation horizon. A changed
   number of raw occupied components is not permission to change expected object
   count. An extra, missing, wrongly phased or mislocated instance is a failure.
3. **Declared symmetry scope.** Rotation/reflection checks must transform supports
   and displacement vectors and respect lattice shape/topology. State which
   symmetries are claimed. Coordinate normalization must not hide excluded
   boundaries, a different horizon, or an altered external context.
4. **Isolation under spacing changes.** Prespecify spacing cases with independently
   justified unchanged operational labels and a finite interaction-free horizon.
   A radius threshold that merges known separate targets or splits the chosen
   compound target fails that endpoint. Once context genuinely changes the
   trajectory, unchanged counts/type labels are not automatically the right
   expectation; classify that case separately rather than forcing invariance.

Known failures are development regressions. Additional authored phases,
translations and spacings may be prospective checks of these relations, but they
are correlated views of selected fixtures. Report results by base family and
transformation. Neither their number nor the number of adjacent frames creates
an iid sample, blinded discovery, or a population performance interval.

## Fair comparison, ablations, and preserved failures

Compare the previous localized method and the revised method on identical raw
trajectories, reference times, truth masks/signatures, admissible conditions and
matching rules. Freeze output adapters, candidate/compute budgets, exclusions
and abstentions. A larger proposal search can improve recall while adding
duplicate/compound candidates; preserve proposal counts, runtime, pruning and
all unmatched outputs. Do not compare only each method's favorable subset.

Useful ablations isolate one change at a time: snapshot component proposals;
the same proposals plus recurrence; temporal association disabled; phase handling
disabled; and a prespecified grouping-radius variant. Apply only ablations that
the implementation actually supports, describe altered semantics, and reuse the
same scorer. An ablation that changes several stages does not isolate one cause.
No supplied ablation establishes superiority over unimplemented domain filters,
local causal states, or sensitivity methods (HC1–HC4, S1–S2, R1–R3).

Match actual reference footprints and declared recurrence signatures one-to-one.
Keep type recognition, instance matching, count agreement, merges, splits,
duplicates, false positives, false negatives and abstentions distinct. If a
signature has symmetric alternatives, freeze its accepted equivalence class;
canonicalize positions only for symmetry checks, not for discarding spatial
identity during same-frame matching. Count agreement alone is not success.

An explicitly fixed mask convention can support a reproducible engineered score
even though physical individuality remains unsettled. For prespecified ambiguous
cases, retain raw predictions and admissible alternatives outside supervised
denominators unless the scoring treatment was frozen. Clutter, collisions,
overlap, seam crossing and short windows are not automatically negative labels.
Use null for undefined ratios. Archive original failures and amendments before
repairs; do not rename known regressions held-out or erase a loss in precision
to highlight recovered recall.

## Negative findings and boundary of the contribution

- Phase-aware particle recognition, particle/subparticle interpretations and
  representation-dependent structure descriptions already exist in the checked
  prior work. Broad novelty of these ideas is unsupported.
- Correct phase-normalized geometry does not establish physical identity,
  causal autonomy, actual interaction or unique decomposition. Those questions
  remain unresolved even if all finite invariance checks pass.
- The old nearby-block/toad cases cannot support an untouched-generalization
  claim after being used to motivate changes. Unexpected new failures and false
  positives are equally material outcomes and must survive the PR handoff.
- This memo has not verified a new detector or theorem, reproduced source
  algorithms, measured H1–H3, or inspected cycle-003 simulation results. Broader
  prior-method comparisons and identity/ancestry interventions remain future work,
  not implicitly authorized experiments.

Independent source/claim review and a separate contribution PR complete this
workstream. No merge, Stage C run, publication, or cycle 004 is authorized by it.
