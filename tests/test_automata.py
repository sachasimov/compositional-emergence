import json
import numpy as np
import pytest
from compositional_emergence.automata import life_step, eca_step
from compositional_emergence.structures import exact_translational_recurrence, Recurrence
from compositional_emergence.simulate import main

def grid(points, n=20):
    a = np.zeros((n,n), dtype=np.uint8)
    for y,x in points: a[y,x] = 1
    return a

def test_block():
    a = grid([(6,6),(6,7),(7,6),(7,7)])
    assert np.array_equal(life_step(a), a)
    assert exact_translational_recurrence(a) == Recurrence(1,(0,0))

def test_blinker():
    a = grid([(7,6),(7,7),(7,8)])
    assert not np.array_equal(life_step(a), a)
    assert np.array_equal(life_step(life_step(a)), a)
    assert exact_translational_recurrence(a) == Recurrence(2,(0,0))

def test_glider():
    a = grid([(6,7),(7,8),(8,6),(8,7),(8,8)])
    b = a.copy()
    for _ in range(4): b = life_step(b)
    assert np.array_equal(b, np.roll(a, (1,1), axis=(0,1)))
    assert exact_translational_recurrence(a) == Recurrence(4,(1,1))

def test_empty_control():
    assert exact_translational_recurrence(np.zeros((20,20), dtype=np.uint8)) is None

def test_eca_90():
    assert np.array_equal(eca_step(np.array([0,0,1,0,0],dtype=np.uint8),90), np.array([0,1,0,1,0],dtype=np.uint8))

def test_reproducible_cli(capsys):
    args=["--system","eca","--rule","110","--size","20","--steps","4","--seed","7"]
    main(args); first=json.loads(capsys.readouterr().out)
    main(args); second=json.loads(capsys.readouterr().out)
    assert first == second
    assert len(first["population_counts"]) == 5
    assert first["status"] == "baseline-simulation-not-a-scientific-result"

def test_invalid_state():
    with pytest.raises(ValueError): life_step(np.zeros((2,2),dtype=np.uint8))
    with pytest.raises(ValueError): eca_step(np.zeros(10,dtype=np.uint8),256)
