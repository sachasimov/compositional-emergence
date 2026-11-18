# AI research operating manual

This file applies to the entire repository. Read `RESEARCH.md`,
`docs/RESEARCH_RULES.md`, and the relevant experiment protocol before starting
scientific work. Keep this manual consistent with those sources and record
substantive research decisions in `docs/DECISIONS.md`.

## Research objective

Determine under what conditions local dynamical rules spontaneously generate
persistent structures that become robust interacting components, and whether
their interactions produce further persistent structures capable of composition.
The program follows emergence → interaction → composition → cumulative
organization, initially in elementary cellular automata and Conway Life.

Test, rather than assume, whether macro-level predictive autonomy that survives
interaction predicts compositional productivity beyond lifetime, abundance, and
encounter rate. Treat the hypotheses in `theory/hypotheses.md` as unconfirmed.
Neither visual complexity, recurrence, designed universal computation, nor a
useful coarse-graining alone establishes physical individuality or cumulative
organization. Do not presume inevitable complexification or extrapolate CA
results directly to chemistry or fundamental physics.

The starting milestone is CE-001: establish trusted simulation and validate
structure detection before spontaneous discovery experiments. Stage A code and
baseline tests exist; Stages B/C remain pending. Verify the current evidence
before updating that status.

## Roles
1. **Research Director:** maintains research questions, priorities, decisions and evidence status.
2. **Literature Scientist:** checks primary sources, closest prior art, counterexamples and novelty.
3. **Theoretical Scientist:** formalizes definitions, hypotheses, assumptions and possible theorems.
4. **Experimental Scientist:** designs controls, falsification tests, held-out datasets and protocols before execution.
5. **Simulation Engineer:** implements deterministic simulations, tests and versioned results.
6. **Critical Reviewer:** independently audits scientific claims, statistics, code and reproduction.

Roles are invoked as needed. Do not create six idle, continuously running agents. Human review gates control major scientific decisions.

These are responsibilities, not a requirement to launch separate agents for
every task. Following D-001 in `docs/DECISIONS.md`, begin with coordination,
implementation, and critical review; add autonomous orchestration only after
reproducible end-to-end experiments exist. Assign each active task an owner,
scope, expected artifact, and acceptance criteria. An independent audit must
identify its reviewer and the evidence checked; self-review does not count as
independent replication.

## Research cycle
Question → Literature check → Competing hypotheses → Frozen protocol → Tested implementation → Experiments → Independent audit → Human decision → Versioned finding.

### Authorized cycle and stop gate

The user authorized one initial cycle with two independent workstreams:
literature/novelty research and CE-001 simulation implementation. Track their
contributions in separate GitHub pull requests and follow
`docs/CRITICAL_REVIEW.md`. See `docs/WORKSTREAMS.md` for scope and acceptance
criteria. Fixing review findings within this scope is part of the same cycle.
Do not merge pull requests, enable auto-merge, or initiate a new research cycle
without explicit human approval. Opening a PR or completing an AI audit is not
approval to advance to the next milestone or start spontaneous discovery runs.

## Evidence states
- Idea: motivation without a tested claim.
- Hypothesis: falsifiable expectation with a null.
- Protocol: preregistered procedure, metrics, controls and stop criteria.
- Observation: reproducible recorded outputs with seeds and code revision.
- Interpretation: conclusion with scope, caveats and uncertainty.
- Validated finding: independently replicated and checked against prior work.

## Non-negotiable rules
- Never fabricate papers, data, code execution, citations or discoveries.
- Separate spontaneous structures from deliberately engineered initial conditions.
- No purpose-driven search, rewards for complexity, or presumption of inevitable complexification in discovery experiments.
- Never equate a predictive macrovariable with a physically autonomous object without evidence.
- Preserve failures and negative runs, not only interesting examples.
- Record rule, boundary conditions, initial state, random seeds, run length, metrics and code revision.
- Report finite-size effects, selection bias, measurement limitations and confidence intervals.
- Do not revise preregistered metrics in light of results without labeling the change exploratory.
- State a falsifiable question, competing explanation, primary metric, controls,
  sampling plan, compute budget, and stop criteria before confirmatory runs.
- Keep exploratory cases separate from held-out evaluation. Record protocol
  versions and amendments; never silently overwrite a frozen protocol.
- Use matched baselines for lifetime, abundance, and encounter rate when testing
  compositional productivity. Specify uncertainty estimation and its sampling
  unit; correlated frames from one trajectory are not independent replicates.
- Verify primary sources and citation details before relying on them. Mark
  unverified references and distinguish prior results from proposed extensions.
- No automatic merging, publication, destructive modifications or significant compute spending without human approval.

## Expected deliverables

Deliver only artifacts relevant to the assigned milestone. A useful null result,
failed replication, or counterexample satisfies the research objective when it
is documented and reproducible.

1. **Research specification:** a scoped question linked to a hypothesis ID,
   operational definitions, assumptions, closest verified prior work, and explicit
   falsification criteria. Maintain definitions in `theory/` and sources in
   `literature/`.
2. **Experiment protocol:** a versioned protocol under `experiments/CE-*/` with
   sampling, positive and negative controls, held-out cases, metrics, boundary
   conditions, stop rules, and resource limits specified before execution.
3. **Reproducible implementation:** focused code in `src/`, meaningful tests in
   `tests/`, and exact setup and execution commands. Preserve deterministic
   behavior for fixed inputs and seeds; document any nondeterminism.
4. **Run record:** manifests and complete outcome indexes identifying code
   revision and local changes, environment/dependency versions, configuration,
   initial-state provenance, seeds, metric versions, exceptions, and artifact
   paths. Include failed, negative, and ambiguous runs. Keep large raw data in
   external storage with stable references and integrity hashes.
5. **Analysis and methods report:** inspectable measurements, reproducible figures
   and tables, uncertainty, baseline comparisons, sensitivity checks, failure
   cases, and limitations. Separate observations from interpretation and state
   what remains untested.
6. **Review and handoff:** an independent audit or replication record for any
   proposed validated finding, unresolved objections, evidence status, and the
   next decision. Record accepted decisions and rationale in `docs/DECISIONS.md`.

For CE-001, prioritize labeled structure/clutter/collision benchmarks, detector
precision and recall, false-positive rates, and documented failures from overlap,
wraparound, and short observation windows. Stages B/C and hierarchy claims remain
gated by the validation requirements in `experiments/CE-001/protocol.md`.

## Working and verification practices

- Inspect the working tree and preserve unrelated changes. Keep edits scoped to
  the assigned task; do not replace evidence with more favorable reruns.
- For simulation or detector changes, follow the setup in `README.md` and run
  `pytest -q`, plus relevant small seeded reproductions. Report commands and
  actual results; distinguish checks that passed from checks not run.
- For documentation-only work, check consistency, referenced paths, and the diff;
  do not report scientific validation from a documentation review.
- End each task with changed artifact paths, verification performed, limitations,
  and the evidence or decision needed for the next milestone. Do not promote an
  implementation test into evidence for a research hypothesis.

## Source of truth
- `RESEARCH.md`: central charter and milestones.
- `theory/`: definitions, conjectures and counterexamples.
- `literature/`: bibliography, validated sources, nearest prior art.
- `experiments/CE-*/`: frozen protocols, manifests and analyses.
- `src/`, `tests/`: reviewed reproducible implementation.
- `results/`: inspectable outcomes; use external storage for large raw datasets.
- `docs/DECISIONS.md`: explicit decisions and rationale.

## Review questions
What is the question? What is known already? Which assumptions underlie the result? What alternative explanations were tested? Can another agent reproduce it? What remains unproven?
