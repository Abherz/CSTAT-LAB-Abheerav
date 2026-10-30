import numpy as np
arr = np.array([1,2,3,4,5])
n = int(input("Enter n: "))
print(f"{n}-th order difference: ", np.diff(arr, n))