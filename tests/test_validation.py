import json

import numpy as np
import pytest

from compositional_emergence.automata import eca_step, life_step
from compositional_emergence.provenance import state_hash
from compositional_emergence.simulate import main
from compositional_emergence.structures import exact_translational_recurrence


@pytest.mark.parametrize("bad", [0.5, -1, 256, 257, np.nan, np.inf, "1"])
def test_rejects_values_before_lossy_conversion(bad):
    for operation, shape in [(life_step, (3, 3)),
                             (lambda x: eca_step(x, 90), (3,)),
                             (exact_translational_recurrence, (3, 3))]:
        a = np.zeros(shape, dtype=object if isinstance(bad, str) else float)
        a.flat[0] = bad
        with pytest.raises(ValueError):
            operation(a)


@pytest.mark.parametrize("period,shift", [(0, 1), (1, -1), (1.5, 1), (2, 0.5), (True, 1)])
def test_invalid_recurrence_limits_even_for_empty_grid(period, shift):
    with pytest.raises(ValueError):
        exact_translational_recurrence(np.zeros((3, 3)), period, shift)


def test_all_eca_neighborhoods_and_rule_bits():
    # Explicit lookup independent of vectorized bit construction and np.roll.
    for rule in range(256):
        truth = [int(bit) for bit in f"{rule:08b}"[::-1]]
        for neighborhood in range(8):
            left, center, right = (int(bit) for bit in f"{neighborhood:03b}")
            state = np.array([left, center, right], dtype=np.uint8)
            result = eca_step(state, rule)
            assert result[1] == truth[neighborhood]
            assert np.array_equal(state, [left, center, right])


def test_life_matches_scalar_toroidal_reference_and_preserves_input():
    rng = np.random.Generator(np.random.PCG64(123))
    for shape in [(3, 3), (4, 7), (9, 9)]:
        a = rng.integers(0, 2, size=shape, dtype=np.uint8)
        original = a.copy()
        expected = np.zeros_like(a)
        for y in range(shape[0]):
            for x in range(shape[1]):
                neighbors = sum(int(a[(y+dy) % shape[0], (x+dx) % shape[1]])
                                for dy in [-1, 0, 1] for dx in [-1, 0, 1]
                                if (dy, dx) != (0, 0))
                expected[y, x] = neighbors == 3 or (a[y, x] == 1 and neighbors == 2)
        assert np.array_equal(life_step(a), expected)
        assert np.array_equal(a, original)


@pytest.mark.parametrize("system", ["eca", "life"])
def test_manifest_replays_full_state_and_records_hashes(system, capsys):
    main(["--system", system, "--size", "8", "--steps", "5", "--seed", "7"])
    result = json.loads(capsys.readouterr().out)
    state = np.array(result["initial_state"], dtype=np.uint8)
    assert state_hash(state) == result["initial_state_sha256"]
    for _ in range(result["steps"]):
        state = life_step(state) if system == "life" else eca_step(state, result["rule"])
    assert np.array_equal(state, result["final_state"])
    assert state_hash(state) == result["final_state_sha256"]
    assert result["provenance"]["source_sha256"]["automata.py"]
    assert result["provenance"]["numpy"] == np.__version__


def test_cli_rejects_negative_seed():
    with pytest.raises(SystemExit):
        main(["--system", "life", "--seed", "-1"])
