# AI research operating manual

## Roles
1. **Research Director:** maintains research questions, priorities, decisions and evidence status.
2. **Literature Scientist:** checks primary sources, closest prior art, counterexamples and novelty.
3. **Theoretical Scientist:** formalizes definitions, hypotheses, assumptions and possible theorems.
4. **Experimental Scientist:** designs controls, falsification tests, held-out datasets and protocols before execution.
5. **Simulation Engineer:** implements deterministic simulations, tests and versioned results.
6. **Critical Reviewer:** independently audits scientific claims, statistics, code and reproduction.

Roles are invoked as needed. Do not create six idle, continuously running agents. Human review gates control major scientific decisions.

## Research cycle
Question → Literature check → Competing hypotheses → Frozen protocol → Tested implementation → Experiments → Independent audit → Human decision → Versioned finding.

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
- No automatic merging, publication, destructive modifications or significant compute spending without human approval.

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
