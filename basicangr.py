#!/usr/bin/python
import angr

binary = "asdf"
proj = angr.Project("asdf", load_options={"auto_load_libs": False})
sim = proj.factory.simulation_manager()

# lambda state: state.posix.dumps(1).find("flag")
win_func = 0x400A71
sim.explore(find=win_func)

# d = sim.deadended[0]
# print(d.trace)

f = sim.found
print(f)
for i in f:
    print(i.state.posix.dumps(0))
