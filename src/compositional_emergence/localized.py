"""Conservative window-start localized recurrence candidates in Life data.

This geometric assay neither identifies physical individuals nor tracks births.
It deliberately abstains beyond its finite isolation and segmentation regime.
"""
from dataclasses import asdict

import numpy as np

from .automata import binary_state, life_step
from .provenance import state_hash
from .structures import exact_translational_recurrence


def components(state, radius=2):
    """Nonperiodic Chebyshev-connected supports, sorted deterministically.

    Radius two groups supports whose Life neighborhoods can overlap. Boundary
    candidates are subsequently abstained from rather than unwrapped.
    """
    remaining = {tuple(map(int, p)) for p in np.argwhere(state)}
    groups = []
    offsets = [(dy, dx) for dy in range(-radius, radius+1)
               for dx in range(-radius, radius+1) if (dy, dx) != (0, 0)]
    while remaining:
        first = min(remaining)
        remaining.remove(first)
        group, queue = {first}, [first]
        while queue:
            y, x = queue.pop()
            for dy, dx in offsets:
                point = y+dy, x+dx
                if point in remaining:
                    remaining.remove(point)
                    group.add(point)
                    queue.append(point)
        groups.append(group)
    return sorted(groups, key=lambda g: min(g))


def support_state(support, shape):
    result = np.zeros(shape, dtype=np.uint8)
    if support:
        ys, xs = zip(*support)
        result[ys, xs] = 1
    return result


def detect_candidates(trajectory, max_period=4, max_shift=2, min_cycles=2,
                      edge_margin=2, max_span=8):
    """Identify isolated t=0 supports recurrent for at least two observed cycles.

    Each t=0 radius-two component must be eight-connected. Its isolated Life
    evolution must equal exactly one radius-two component of every observed
    frame. Later contacts, splits, edge proximity and large supports cause an
    abstention for the whole track. This loses legitimate multipart/phase-shifted
    oscillators and nearby objects; every initial support receives a disposition.
    """
    data = binary_state(trajectory)
    if data.ndim != 3 or data.shape[0] < 1 or min(data.shape[1:]) < 5:
        raise ValueError("trajectory must have shape (time>=1, height>=5, width>=5)")
    bounds = [(max_period, 1), (max_shift, 0), (min_cycles, 2),
              (edge_margin, 1), (max_span, 1)]
    if any(isinstance(x, (bool, np.bool_)) or not isinstance(x, (int, np.integer))
           or x < lower for x, lower in bounds):
        raise ValueError("integer limits required; min_cycles>=2 and edge_margin>=1")
    for t in range(len(data)-1):
        if not np.array_equal(life_step(data[t]), data[t+1]):
            raise ValueError(f"trajectory violates Life B3/S23 at step {t+1}")
    segmented = [components(frame) for frame in data]
    tracks = []
    for index, support in enumerate(segmented[0]):
        initial = support_state(support, data.shape[1:])
        row = {"track_id": index, "initial_live_cells": [list(p) for p in sorted(support)],
               "initial_sha256": state_hash(initial), "status": "candidate",
               "reason": None, "failure_frame": None, "recurrence": None,
               "support_sha256_by_frame": []}
        def stop(reason, frame, status="abstained"):
            row.update(status=status, reason=reason, failure_frame=frame)
        if len(components(initial, radius=1)) != 1:
            stop("initial-segmentation-ambiguity", 0)
        else:
            predicted = initial.copy()
            for t, groups in enumerate(segmented):
                points = {tuple(map(int, p)) for p in np.argwhere(predicted)}
                if not points:
                    stop("extinct-before-window-end", t, "rejected-transient")
                    break
                ys, xs = zip(*points)
                if (min(ys) < edge_margin or min(xs) < edge_margin or
                    max(ys) >= data.shape[1]-edge_margin or
                    max(xs) >= data.shape[2]-edge_margin):
                    stop("boundary-proximity", t)
                    break
                if max(max(ys)-min(ys)+1, max(xs)-min(xs)+1) > max_span:
                    stop("support-exceeds-localization-bound", t)
                    break
                if sum(points == group for group in groups) != 1:
                    stop("interaction-or-segmentation-change", t)
                    break
                row["support_sha256_by_frame"].append(state_hash(predicted))
                if t < len(data)-1:
                    predicted = life_step(predicted)
            if row["status"] == "candidate":
                found = exact_translational_recurrence(initial, max_period, max_shift)
                if found is None:
                    stop("no-initial-recurrence-within-bounds", len(data)-1)
                elif min_cycles * found.period > len(data)-1:
                    stop("insufficient-observed-cycles", len(data)-1)
                else:
                    row["recurrence"] = asdict(found)
        tracks.append(row)
    return {"method": "window-start-isolated-local-recurrence-v1", "tracks": tracks,
            "candidate_count": sum(r["status"] == "candidate" for r in tracks),
            "parameters": {"max_period": max_period, "max_shift": max_shift,
                           "min_cycles": min_cycles, "edge_margin": edge_margin,
                           "max_span": max_span},
            "observed_frames": len(data), "tracked_births": False}
