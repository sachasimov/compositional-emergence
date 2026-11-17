# CE-001 preregistration draft — CA baseline and object detection

**Question:** Can coherent persistent patterns be identified without conflating static recurrence, random clutter and interacting objects?

## Stage A — trusted simulation
- Elementary cellular automata: periodic ring and Wolfram index mapping neighborhood `000` to bit 0, `111` to bit 7.
- Conway Life: eight-neighbor update and periodic two-dimensional boundary.
- Confirm empty state, still-life block, blinker (period 2), glider (period 4, displacement (1,1)), and Rule 90.
- Record seeds, initial conditions, parameters and run manifests.

## Stage B — object detector validation
- Define candidate events and an annotation method before testing.
- Construct isolated patterns, collisions, random clutter, and empty negative controls.
- Quantify precision, recall, false-positive rate, timing and failures from overlapping structures, periodic wraparound and insufficient windows.
- Maintain separate exploratory and held-out cases.

## Stage C — spontaneous runs (only after Stage B)
- Choose a prespecified sample of ECA rules and 2D rules.
- Vary density, lattice size, horizon, seeds, and boundary conditions.
- Compare detected structures with simple occupancy and persistence baselines.
- Keep complete run logs, positive, negative and ambiguous results.

## Stop condition
No claims about compositional hierarchies until object identity and event tracking have been validated. Exact translational recurrence is a limited sanity check, not a discovery engine.

**Status:** Stages B/C are pending; starter simulation code has baseline tests.
