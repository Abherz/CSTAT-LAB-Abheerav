import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,15)
y = x*x

plt.title("Line graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.plot(x, y, color="blue")
plt.show()