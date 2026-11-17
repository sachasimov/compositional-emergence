"""Minimal deterministic cellular automata with explicit periodic boundaries."""
import numpy as np

def life_step(state: np.ndarray) -> np.ndarray:
    """One B3/S23 Game of Life update on a 2-D toroidal grid."""
    a = np.asarray(state, dtype=np.uint8)
    if a.ndim != 2 or min(a.shape) < 3:
        raise ValueError("Life requires a 2-D grid at least 3x3")
    if not np.isin(a, [0, 1]).all():
        raise ValueError("Life states must be binary")
    neighbors = np.zeros_like(a, dtype=np.int16)
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if (dy, dx) != (0, 0):
                neighbors += np.roll(a, shift=(dy, dx), axis=(0, 1))
    return ((neighbors == 3) | ((a == 1) & (neighbors == 2))).astype(np.uint8)

def eca_step(state: np.ndarray, rule: int) -> np.ndarray:
    """ECA update on a periodic ring, using Wolfram's numbering."""
    a = np.asarray(state, dtype=np.uint8)
    if a.ndim != 1 or a.size < 3:
        raise ValueError("ECA requires a 1-D ring with at least 3 cells")
    if not np.isin(a, [0, 1]).all():
        raise ValueError("ECA states must be binary")
    if not isinstance(rule, (int, np.integer)) or not 0 <= rule <= 255:
        raise ValueError("ECA rule must be an integer in [0, 255]")
    left, right = np.roll(a, 1), np.roll(a, -1)
    neighborhood = (left << 2) | (a << 1) | right
    return ((rule >> neighborhood) & 1).astype(np.uint8)
