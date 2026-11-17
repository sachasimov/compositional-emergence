# Compositional Emergence

**Research question:** What distinguishes dynamical systems that exhibit complex patterns from systems that spontaneously generate persistent, interacting structures capable of participating in further composition?

A research program on **emergence → interaction → composition → cumulative organization**, initially using cellular automata as controlled, non-teleological model systems.

## The scientific claim we want to test—not assume

A persistent pattern is not automatically a new physical building block. Likewise, a useful coarse-grained description is not automatically an autonomous object. We want to test whether robust macro-level dynamics under interaction help predict which emergent patterns can serve as components for further structure formation.

We do **not** assume the universe optimizes complexity, performs purposeful search, or becomes progressively more complex. Random initial conditions, local rules, and physical constraints are enough to define the systems we study.

## Start here

- [RESEARCH.md](RESEARCH.md): agenda, questions, hypotheses and milestones.
- [AGENTS.md](AGENTS.md): roles, permissions and review workflow for AI-assisted research.
- [theory/definitions.md](theory/definitions.md): tentative, explicitly operational definitions.
- [literature/README.md](literature/README.md): reading map and verification tasks.
- [experiments/CE-001/protocol.md](experiments/CE-001/protocol.md): first benchmark protocol.
- [issues/CE-001.md](issues/CE-001.md): initial GitHub issue draft.

## Running the starter simulator

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest -q
python -m compositional_emergence.simulate --system life --size 40 --steps 20 --seed 42
python -m compositional_emergence.simulate --system eca --rule 110 --size 80 --steps 30 --seed 42
```

This initial code is a **verified simulation baseline**, not an automated discovery engine and not evidence for any scientific hypothesis. It includes 2-D Conway Life, 1-D elementary cellular automata and a deliberately narrow detector of exact translational recurrence for isolated patterns. A general detector for spontaneous objects remains part of CE-001.

## Scientific standards

- Separate hypotheses, observations, interpretations, and speculation.
- Record rule definitions, boundary conditions, random seeds, code revision and metric versions.
- Compare against nulls and controls; keep negative results.
- Review the literature before declaring a result original.
- Require independent replication before promoting a result into accepted findings.
- No human-selected target structure or reward for visual complexity in discovery experiments.

## Reference papers

- Rosas (2026), [*Symmetry as a common origin of hierarchical emergence and abstraction*](https://doi.org/10.1126/sciadv.aeh0773).
- Rosas et al. (2024), [*Software in the natural world: A computational approach to hierarchical emergence*](https://arxiv.org/abs/2402.09090).
- Israeli & Goldenfeld (2006), [*Coarse-graining of cellular automata, emergence, and the predictability of complex systems*](https://doi.org/10.1103/PhysRevE.73.026203).
- Simon (1962), *The Architecture of Complexity*.
- Brian Potter, [*Information and Technological Evolution*](https://www.construction-physics.com/p/information-and-technological-evolution), as motivation—not evidence of a universal physical law.

## Status

**Stage:** Research foundation / CE-001 planned. No original discovery or universal claim has been established.
