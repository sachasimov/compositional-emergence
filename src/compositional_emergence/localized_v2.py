"""Finite geometric candidates from overlap-connected spacetime components.

Spatial/temporal edges are bookkeeping, not causal links. Internal decomposition
is not unique, and recurrent composite supports may falsely fuse supplied objects.
The cycle-002 detector in localized.py remains unchanged as a versioned baseline.
"""
from collections import Counter, defaultdict
from dataclasses import asdict

import numpy as np

from .automata import binary_state, life_step
from .localized import components, support_state
from .provenance import state_hash
from .structures import exact_translational_recurrence


def spacetime_groups(data, association="overlap-union"):
    """Group eight-components through shared live coordinates in adjacent frames.

    The ablation retains an edge only when its endpoints are each incident to
    one overlap edge across that frame transition. Everything else is identical.
    """
    if association not in ("overlap-union", "one-to-one-overlap"):
        raise ValueError("unknown association mode")
    nodes, by_frame = [], []
    for t, frame in enumerate(data):
        indices = []
        for support in components(frame, radius=1):
            indices.append(len(nodes))
            nodes.append((t, support))
        by_frame.append(indices)
    parent = list(range(len(nodes)))
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    all_edges, selected = [], []
    for t in range(len(data)-1):
        left = {p: i for i in by_frame[t] for p in nodes[i][1]}
        right = {p: i for i in by_frame[t+1] for p in nodes[i][1]}
        edges = sorted({(left[p], right[p]) for p in left.keys() & right.keys()})
        left_degree = Counter(a for a, _ in edges)
        right_degree = Counter(b for _, b in edges)
        for a, b in edges:
            all_edges.append((a, b))
            if association == "overlap-union" or left_degree[a] == right_degree[b] == 1:
                selected.append((a, b))
                ra, rb = root(a), root(b)
                if ra != rb:
                    parent[rb] = ra
    grouped = defaultdict(list)
    for i in range(len(nodes)):
        grouped[root(i)].append(i)
    # Stable temporal/spatial order, independent of union-find representative.
    groups = sorted(grouped.values(), key=lambda indices:
                    min((nodes[i][0], min(nodes[i][1])) for i in indices))
    return nodes, groups, {"spatial_component_nodes": len(nodes),
                           "observed_overlap_edges": len(all_edges),
                           "selected_overlap_edges": len(selected)}


def detect_candidates_v2(trajectory, max_period=4, max_shift=2, min_cycles=2,
                         edge_margin=2, max_span=8, association="overlap-union"):
    """Test complete observed graph groups against isolated initial evolution.

    Group selection uses the whole observation window. A group without t=0
    support is explicitly abstained from. For every other group, isolated Life
    evolution must equal the COMPLETE observed group support at every frame.
    Births, recurrence after a transient, boundaries and causal autonomy are not
    inferred. A temporal union can join multipart phases or merge independent
    objects; a matching recurrent union is not a certificate of unique identity.
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
    nodes, groups, graph = spacetime_groups(data, association)
    tracks = []
    for index, indices in enumerate(groups):
        supports = [set() for _ in data]
        counts = [0 for _ in data]
        for i in indices:
            t, points = nodes[i]
            supports[t].update(points)
            counts[t] += 1
        first = next(t for t, points in enumerate(supports) if points)
        initial = support_state(supports[0], data.shape[1:])
        row = {"track_id": index,
               "initial_live_cells": [list(p) for p in sorted(supports[0])],
               "first_observed_frame": first,
               "first_observed_live_cells": [list(p) for p in sorted(supports[first])],
               "initial_sha256": state_hash(initial),
               "spatial_component_count_by_frame": counts,
               "multipart_at_some_frame": max(counts) > 1,
               "support_sha256_by_frame": [state_hash(support_state(points, data.shape[1:]))
                                            for points in supports],
               "status": "candidate", "reason": None, "failure_frame": None,
               "recurrence": None}
        def stop(reason, frame, status="abstained"):
            row.update(status=status, reason=reason, failure_frame=frame)
        if not supports[0]:
            stop("no-window-start-support", first)
        else:
            predicted = initial.copy()
            for t in range(len(data)):
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
                if points != supports[t]:
                    stop("complete-observed-group-disagreement", t)
                    break
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
    return {"method": "overlap-connected-spacetime-recurrence-v2", "association": association,
            "tracks": tracks, "candidate_count": sum(t["status"] == "candidate" for t in tracks),
            "parameters": {"max_period": max_period, "max_shift": max_shift,
                           "min_cycles": min_cycles, "edge_margin": edge_margin,
                           "max_span": max_span}, "graph": graph,
            "observed_frames": len(data), "tracked_births": False,
            "graph_edges_are_causal_links": False}
