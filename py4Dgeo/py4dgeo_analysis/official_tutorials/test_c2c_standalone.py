"""
Standalone repro of the C2C crash, run OUTSIDE Jupyter so the real
error/segfault message isn't swallowed by the VS Code Jupyter extension.

Run from Terminal:
    /opt/anaconda3/envs/quintaplaya/bin/python test_c2c_standalone.py

(or `conda activate quintaplaya` first, then `python test_c2c_standalone.py`)
"""

import sys
import platform

print("=" * 60)
print("Python:", sys.version)
print("Machine:", platform.machine())
print("=" * 60)

print("\n[1] Importing py4dgeo...")
import py4dgeo
print("    OK -", py4dgeo)

print("\n[2] Downloading/locating tiny plane_horizontal test data...")
t1 = py4dgeo.find_file("plane_horizontal_t1.xyz")
t2 = py4dgeo.find_file("plane_horizontal_t2.xyz")
print("    OK -", t1, t2)

print("\n[3] Reading epochs...")
epoch0, epoch1 = py4dgeo.read_from_xyz(t1, t2)
print("    OK - epoch0:", epoch0.cloud.shape, "epoch1:", epoch1.cloud.shape)

print("\n[4] Building corepoints subset...")
corepoints = epoch0.cloud[::25]
print("    OK -", corepoints.shape)

print("\n[5] Instantiating C2C...")
c2c = py4dgeo.C2C(
    epochs=(epoch0, epoch1),
    corepoints=corepoints,
    max_distance=3.0,
)
print("    OK")

print("\n[6] Running C2C.run() -- this is where it's been crashing...")
distances = c2c.run()
print("    OK - distances:", distances.shape)

print("\nAll steps completed successfully.")
