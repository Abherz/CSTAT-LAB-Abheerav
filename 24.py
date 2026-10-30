import numpy as np

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

result = np.einsum("mk,kn", array1, array2)
print("Einstein's summation convention:\n", result)