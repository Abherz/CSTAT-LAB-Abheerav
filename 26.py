import numpy as np

data = np.random.randint(10, size=5)
print(data)
mean_val = np.mean(data)
var_val = np.var(data)
std_val = np.std(data)

print(f"Mean: {mean_val:.2f}")
print(f"Variance: {var_val:.2f}")
print(f"Standard Deviation: {std_val:.2f}")