import numpy as np

rng = np.random.default_rng(seed=42)
xarr = rng.random((3, 3))
R1 = np.corrcoef(xarr)
print(R1)