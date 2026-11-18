# Independent critical review — initial research cycle

Date: 2026-11-18. Reviewer: Codex agent `/root/critical_review`, independent of
the Literature Scientist and Simulation Engineer agents. This is an AI audit,
not a human approval or a claim of independent scientific replication across
implementations.

## Reviewed contributions

| Contribution | Submitted revision | Review status |
|---|---|---|
| [Governance PR #2](https://github.com/sachasimov/compositional-emergence/pull/2) | `c78cce92727aa4c8ef6e918f6458a1a2adc234cd` | Documentation audit complete; no blocking finding |
| [Literature PR #4](https://github.com/sachasimov/compositional-emergence/pull/4) | `6367fc13c2714e63b4905a40536e7cd819cbd205` | Dossier audit and primary-source spot checks complete; no blocking finding |
| [Simulation PR #3](https://github.com/sachasimov/compositional-emergence/pull/3) | `47c41422a0029bf3d3ab61f257062e1ff1525aaa` | Original/repair independently reproduced; two findings closed |

Neither a PR nor this audit authorizes merging or a new cycle. Governance changes
after `c78cce9` add this review record; no self-audit of this record is claimed.

## Governance audit

Inspected `AGENTS.md`, `docs/WORKSTREAMS.md`, `docs/CRITICAL_REVIEW.md`,
`docs/DECISIONS.md`, the PR template, `RESEARCH.md`, the hypothesis register,
definitions, research rules, and the original CE-001 protocol. Commands:

```bash
git diff c44da4e..c78cce9 --stat
git show --format=fuller --no-patch c78cce9
git status --short
```

The operating instructions require verified claim-level primary-source support,
falsifiable hypotheses, frozen protocols, baseline comparisons, retained negative
outcomes, separate contribution PRs, and an independent reviewer. They explicitly
forbid merging, auto-merge, and a new cycle without human approval. The two
workstreams share a repository baseline but have separate worktrees and scopes.
No blocking governance finding was identified.

Existing H1–H3 are conceptual research hypotheses, not executable confirmatory
protocols. This audit will check scoped falsifiers in the literature dossier and
ensure the initial simulation pilot does not claim to test H2 or establish a
universal H3 conclusion. General object detection, spontaneous composition, and
scientific novelty remain unproven.

## Simulation evidence and reproduction

Created a separate detached worktree at `/workspace/ce-review-simulation` and
ran the package from that worktree via explicit `PYTHONPATH`, using the author's
Python environment only for dependencies. The review environment used the same
Python/NumPy versions and is not an independent CA implementation. Original and
repaired run manifests both identify clean source revisions before execution.

Commands executed (from the review worktree unless specified):

```bash
git worktree add --detach /workspace/ce-review-simulation 2722fbb3ee6644958146fb6624c49507e7510fb3
PYTHONPATH=/workspace/ce-review-simulation/src /workspace/ce-simulation/.venv/bin/python -m pytest -q /workspace/ce-review-simulation/tests
PYTHONPATH=/workspace/ce-review-simulation/src /workspace/ce-simulation/.venv/bin/python -m compositional_emergence.benchmark --output /tmp/ce001-independent-review.json
git switch --detach 2d6e5bf58a361839cbfd226486b82ef41a9c4d01
PYTHONPATH=/workspace/ce-review-simulation/src /workspace/ce-simulation/.venv/bin/python -m pytest -q
PYTHONPATH=/workspace/ce-review-simulation/src /workspace/ce-simulation/.venv/bin/python -m compositional_emergence.benchmark --output /tmp/ce001-independent-review-amendment-1.json
git status --short
```

Results: 26 original tests passed, then 29 repaired tests passed. Both 19-case
pilots completed with all fixture expectations met. A JSON comparison checked
all case IDs, coordinates, input hashes, period/shift limits, labels/splits,
statuses, recurrence signatures, assay and baseline predictions, and metrics
against the preserved original and repaired author artifacts. All matched.
Repaired source SHA-256 values and the amendment SHA-256 matched the author's
repaired run. Elapsed time and Git metadata were excluded from scientific-output
comparisons; the independent repaired run was clean at `2d6e5bf`.

| Fixed scored panel (11 cases) | TP | FP | TN | FN | Accuracy |
|---|---:|---:|---:|---:|---:|
| Exact recurrence assay | 6 | 0 | 5 | 0 | 11/11 |
| Nonempty occupancy | 6 | 4 | 1 | 0 | 7/11 |
| One-step stationarity | 1 | 0 | 5 | 5 | 6/11 |

The other eight cases are explicitly unscored diagnostics. The assay misses a
known blinker with an insufficient time window, a glider without translation,
and independently moving block/glider structure under a single full-grid
translation. Boundary-crossing recurrence is recorded as toroidal behavior,
not proof of free-space identity. Both clutter cases returned no recurrence;
neither was used as a labelled object-detection negative. All these outcomes,
overlap and encounter challenges remain archived. No inference of population
precision/recall or compositional productivity follows from this fixed panel.

The scalar Life comparison and exhaustive ECA rule/neighborhood tests provide
independent expected update behavior, but the pilot reproduction uses the same
recurrence implementation. General detector validation, collision-product
ancestry, finite-size sensitivity, spontaneous discoveries and H1–H3 remain
pending. The weak baselines are appropriately described as limited sanity checks.

## Primary-source spot checks

Independently searched for the two papers below and fetched their full primary
texts on 2026-11-18, then compared their support with the submitted dossier.

- Israeli and Goldenfeld, *Physical Review E* 73, 026203 (2006), DOI
  [10.1103/PhysRevE.73.026203](https://doi.org/10.1103/PhysRevE.73.026203).
  Inspected the [author-hosted journal PDF](https://guava.physics.ucsd.edu/~nigel/REPRINTS/2006/Israeli%20Coarse-graining%20of%20cellular%20automata%20PRE%202006%20%28PDF%29.pdf),
  especially §§III–IV, Eq. (1), and §VI. Exact coarse-graining and the rule-110
  projection to rule 0 are established there; this is not autonomous-object or
  cumulative-composition evidence. The paper distinguishes empirical support
  from formal proof for its broader coarse-grainability argument.
- Shalizi et al., *Automatic Filters for the Detection of Coherent Structure in
  Spatiotemporal Systems*, [arXiv:nlin/0508001v1](https://arxiv.org/pdf/nlin/0508001v1),
  dated 2005-07-29, linked by arXiv to *Physical Review E* 73, 036104 (2006), DOI
  [10.1103/PhysRevE.73.036104](https://doi.org/10.1103/PhysRevE.73.036104).
  Inspected §§II, III, and V. §II explicitly motivates local sensitivity by
  autonomous objects; structure alone need not imply autonomy. Sensitivity and
  statistical-complexity filters recover distinct features. Broad generic
  applicability is described as a hypothesis, not a theorem. The checked full
  text is the arXiv version, not an assertion of final-version identity.

Reviewer searches also located Balduzzi's
[arXiv:1105.0158v2](https://arxiv.org/html/1105.0158v2) on emergent processes in
Life and context-dependent coarse-graining. It was sent to the literature
author as potential prior overlap; it is not evidence that every proposed
compositional-productivity test has already been performed.

Additional submitted-ledger checks used the same connected web-fetch tool on
2026-11-18:

| Source | Material independently checked | Audit outcome |
|---|---|---|
| S1, Rosas 2026 | Institutional accepted-version abstract at its ledger URL | Supports sufficient dynamical-equivariance mechanism and named examples. PDF is request-a-copy; final proofs remain unchecked. No final theorem is asserted by the dossier. |
| S2, Rosas et al. 2024 | Version-pinned arXiv v2, §§III.2–III.5, IV.1 and associated figures | Supports distinctions among closure notions and trivial/nontrivial invariants. Constant macrovariables are a legitimate control, not proof of localized individuality. |
| S4, Hanson and Crutchfield 1997 | Author-hosted journal PDF, §§3–6 and collision table/figures | Supports domains, particles, two-/three-particle collisions, statistics and secondary structures as prior art. Broad particle/collision novelty is properly rejected. |
| S6, Crutchfield 1994 | Author manuscript, Part II §2 and Part III §5.3 | Named locators support metric/model dependence, complexity/randomness distinction, and spatial coherence/filtering examples. Manuscript pagination differs from the journal as disclosed. |
| S7, Cook 2004 | Publisher abstract | Supports Rule 110 universality only. The dossier makes no detailed construction/proof claim. The publisher abstract now links a different PDF route, `https://content.wolfram.com/sites/13/2023/02/15-1-1.pdf`; this reviewer did not audit that proof. The author's recorded failed URL remains a historical access failure. |
| S8, Hintze and Bohm 2025 | Version-pinned arXiv v1, Outlier Rule, Method, Replicator Classification, and boundary discussion | Confirms novelty-search rule selection, selected nonextinguishing c0 seed, cluster ancestry and reported multigeneration replication. The dossier preserves these selection caveats and does not equate replication with broader composition. Final journal version remains unchecked. |

These are independent claim-level checks, not a full rederivation of every paper,
verification of every metadata field, or replication of prior algorithms. The
Rosas 2025 predecessor, Simon, Rupe/Crutchfield and Balduzzi were not fully audited
here. Unresolved leads and access limits remain explicit rather than treated as
evidence that an area is unexplored.

## Literature disposition

At `6367fc13`, all five changed files are literature artifacts. The dossier
clearly distinguishes full-text, abstract-only, inherited, and unchecked sources
and records exact search queries and limitations. It gives scoped falsifiers
for H1–H3, a prospective ancestry/product endpoint, simple covariate baselines,
held-out trajectory/rule-family evaluation, a shuffled-feature control, and
prospective clustered uncertainty. The hypotheses remain proposed tests; sample
size, estimator, rule ensemble, tolerance and budget are deliberately deferred
to a future frozen protocol requiring approval.

Negative novelty conclusions are preserved: structure detection, particles,
collisions, autonomy language and lineages are established prior art. The exact
H2 predictive comparison is only a candidate; targeted search absence is not
novelty evidence. The constant-macrovariable objection and selection confounds
are explicit. No scientific experiment or novel theorem is reported from this
workstream. No blocking literature finding was identified for this bounded
dossier. The unresolved source coverage prevents any stronger novelty claim.

The literature dossier prospectively suggests an always-negative baseline in
addition to occupancy and persistence. The independently specified current
pilot used occupancy and one-step stationarity; on this fixed scored panel an
always-negative classifier would have 0 TP, 0 FP, 5 TN, 6 FN (5/11 accuracy).
This is a transparent arithmetic comparison, not an additional experiment or a
post-hoc improvement to the frozen protocol.

## Findings and resolution history

No blocking governance findings.

| ID | Severity | Finding and consequence | Response and resolution |
|---|---|---|---|
| CR-S1 | MAJOR | At `2722fbb`, P1 names periods/displacements but the automated acceptance flag checked only recurrence presence. Incorrect signatures could pass. | Author preserved the original protocol/output, added explicit expected signatures and a dated review amendment at `2d6e5bf`, and froze that amendment before the repair run. Wrong-period/displacement regressions pass. Reviewer independently checked all signatures and reproduced the repaired panel. **Closed.** |
| CR-S2 | MAJOR | At `2722fbb`, Stage A `simulate --output` silently overwrote existing run files, risking loss of prior/negative evidence. | At `2d6e5bf`, the CLI rejects existing paths and uses exclusive file creation; a regression preserves original bytes on the second attempted run. Code inspection and independent tests passed. **Closed.** |

These are repairs to the same prespecified panel, not newly selected experiments.
The original result is retained; the post-result acceptance repair is explicitly
labelled and cannot retrospectively become an original preregistration.

## Human decision gate

Review of the submitted contributions is complete. The final simulation commit
adds results and documentation only; `git diff --exit-code` confirmed no change
from the independently rerun repair revision to source, tests, or either pilot
protocol. `git diff --check` passed for both workstream diffs. The original
protocol and result are byte-identical to their archived versions; original
result SHA-256 is `fba40684768e6ea89835a3bc0a479e91bd530d41a2a91c652dba2a1a7ecad7a3`.

There are no open blocking findings for accepting these contributions as a
bounded literature assessment and implementation/assay pilot. This recommendation
does not validate a general detector, H1–H3, or a novelty claim. The fixed panel
and same-implementation reproduction have the limits described above.

All three PRs remain subject to human review. Do not merge, enable auto-merge,
run Stage C, or initiate another research cycle. Explicit human approval remains
outstanding; the current cycle stops here.
