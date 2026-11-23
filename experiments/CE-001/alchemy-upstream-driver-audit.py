"""Run against a local pinned AlChemy checkout. No reactor execution."""
import ast
import contextlib
import copy
import io
import json
import os
import pathlib
import sys
import types

source = pathlib.Path(sys.argv[1]) / "PyAlChemy/L2_source/look_for_L2.py"
tree = ast.parse(source.read_text())
node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "run_compositions")
written = {}
def write(comp, ids, name):
    written[name] = copy.deepcopy(comp)
def simulation(*args, **kwargs):
    return dict(name=args[0], seed=args[4], capacity=args[5], collisions=args[6], input=kwargs["input_file"])
env = dict(os=os, RSEED=808, DIRNAME="stub", HEAP_SIZE=800, MAX_STEPS=500,
           pd=types.SimpleNamespace(DataFrame=lambda rows: rows),
           LambdaRandomizer=lambda **kw: kw, LambdaReducer=lambda **kw: kw,
           write_expressions_to_file=write, Simulation=simulation, run_sim=lambda s:s)
exec(compile(ast.Module(body=[node], type_ignores=[]), str(source), "exec"), env)
parents = {x: ({x.lower():10}, {x.lower():0}) for x in "ABCD"}
original = copy.deepcopy(parents)
with contextlib.redirect_stdout(io.StringIO()):
    rows = env["run_compositions"](parents)
result = dict(mixtures=written, runs=rows, parents_unchanged=parents==original,
              unique_seeds=len({r["seed"] for r in rows}),
              valid_pairs=sum(set(v)==set("".join(k.split("_")[:2]).lower()) and sum(v.values())==20 for k,v in written.items()))
print(json.dumps(result, indent=2))
