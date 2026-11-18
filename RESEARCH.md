# Research charter — Compositional Emergence

## Central question
**Under what conditions do local dynamical rules spontaneously produce persistent structures that can become robust interacting components, and when can their interactions produce further persistent structures?**

The scientific focus is **emergence → interaction → composition → cumulative organization**.

## Distinctions
- Complex-looking patterns are not necessarily structured or composed.
- Predictive macroscopic descriptions are not necessarily physical individuals.
- Stable objects are not necessarily productive building blocks.
- Universal computation under designed initial conditions does not imply spontaneous cumulative organization.
- No universal tendency for the universe to seek or optimize complexity is presumed.

## Questions
1. **Identification:** Can coherent persistent entities be detected from unlabelled spacetime data?
2. **Autonomy:** Which higher-level variables describe their dynamics, and how does symmetry or informational closure help?
3. **Coupling:** Does a macrodescription remain predictively sufficient when an object interacts with another?
4. **Composition:** When do encounters generate new persistent, distinguishable objects?
5. **Accumulation:** Can those products themselves participate in productive second- and later-generation interactions without designed targets?
6. **Generality:** Which observations extend across rules, boundary conditions, initial densities and simulation families?

## Working hypotheses (unconfirmed)
- H1: Persistence makes repeated encounters possible but is insufficient to predict compositional productivity.
- H2: Macroscopic predictive autonomy robust to coupling predicts compositional productivity beyond lifetime, abundance, and encounter rate.
- H3: No universal monotonic relation between visual complexity and cumulative organization should be assumed.

The critical null for H2 is that basic lifetimes and encounter rates explain the measured outcomes.

## Models
Begin with elementary cellular automata and Conway Life, followed by selected richer two-dimensional rules and eventually artificial chemical reaction networks. Avoid extrapolating directly from CA to chemistry or physics.

## Milestones
- M0: Literature novelty map, working definitions, controls, falsification criteria.
- M1 / CE-001: Correct simulators, known patterns and negative controls, narrow recurrence detection.
- M2: Track structures from spontaneous initial conditions; measure encounters and products.
- M3: Test whether compositional robustness predicts outcomes better than simpler baselines.
- M4: Replicate and test on held-out rule families; write a carefully scoped paper if warranted.

Advance only when evidence is inspectable, assumptions are explicit, literature checked and an independent review has been completed. A null finding or rigorous counterexample is a valid research outcome.

## Current evidence status — 2026-11-18

Cycle-001 contributions were independently audited and merged with human
approval. Stage A implementation and a small engineered whole-grid recurrence
assay pilot are available; the integrated baseline passes 29 tests. This is
method-validation evidence, not support for H1–H3 or general object detection.
The literature dossier records substantial prior overlap and does not certify
novelty. See `docs/reviews/cycle-001.md` for the audit and its limitations.

One additional bounded cycle is authorized for detector methodology and CE-001
Stage B localized-candidate validation (`docs/cycles/cycle-002.md`). Its new
contributions require independent review and fresh merge approval. Stage C and
later research cycles remain gated.

The user subsequently approved cycle-002 PRs #5–#7 and one targeted continuation.
Integrated `main` at `aeed31d` passes 42 tests. The merged geometric method
matches 13/16 labelled objects in a fixed engineered panel, with three retained
false negatives; this is not general object validation. Cycle 003 addresses
phase/proximity limitations with the previous method as a direct baseline.
See D-007 and `docs/cycles/cycle-003.md`. New contribution merges and any further
cycle require fresh approval.
