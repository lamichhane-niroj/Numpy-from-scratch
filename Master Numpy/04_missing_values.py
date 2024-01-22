# nan is for missing value
import numpy as np

arr = np.array([1, 2, 3, 4, np.nan, 6, 7])

# how to remove this missing value. We can use filtering
print(arr[~np.isnan(arr)])
