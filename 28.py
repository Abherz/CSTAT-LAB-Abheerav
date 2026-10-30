import numpy as np
import pandas as pd

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

df = pd.DataFrame(arr, columns=['Column1', 'Column2', 'Column3'])
df.to_csv('output.csv', index=False)
