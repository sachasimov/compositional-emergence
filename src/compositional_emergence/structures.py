"""Restricted Life recurrence assay; not a general object detector."""
from dataclasses import dataclass
import numpy as np
from .automata import binary_state, life_step

@dataclass(frozen=True)
class Recurrence:
    period: int
    displacement: tuple[int, int]

def exact_translational_recurrence(initial: np.ndarray, max_period: int = 12, max_shift: int = 4) -> Recurrence | None:
    """Check full-grid equality after a time period and spatial translation.

    Only meaningful for selected isolated patterns on sufficiently large grids.
    """
    a = binary_state(initial)
    if a.ndim != 2 or min(a.shape) < 3:
        raise ValueError("expected a 2-D Life grid of at least 3x3")
    if any(isinstance(x, (bool, np.bool_)) or not isinstance(x, (int, np.integer)) for x in (max_period, max_shift)):
        raise ValueError("max_period and max_shift must be integers")
    if max_period < 1 or max_shift < 0:
        raise ValueError("max_period must be >=1 and max_shift >=0")
    if not np.any(a):
        return None
    current = a.copy()
    shifts = [(dy, dx) for dy in range(-max_shift, max_shift + 1) for dx in range(-max_shift, max_shift + 1)]
    shifts.sort(key=lambda pair: (abs(pair[0]) + abs(pair[1]), abs(pair[0]), abs(pair[1]), pair))
    for period in range(1, max_period + 1):
        current = life_step(current)
        for shift in shifts:
            if np.array_equal(current, np.roll(a, shift=shift, axis=(0, 1))):
                return Recurrence(period=period, displacement=shift)
    return None
