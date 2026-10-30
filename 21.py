import numpy as np

arr = np.array([[1, 2, 4], [0, 0, 5], [0, 3, 6]])

print(arr)

q, r = np.linalg.qr(arr)
print('\nQ:\n', q)
print('\nR:\n', r)
print(np.allclose(arr, np.dot(q, r))) 