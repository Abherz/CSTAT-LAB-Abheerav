import numpy as np


mat = np.mat("2 -1;4 2")

print(mat)
print("")
evalue, evect = np.linalg.eig(mat)

print(evalue)
print("")

print(evect)