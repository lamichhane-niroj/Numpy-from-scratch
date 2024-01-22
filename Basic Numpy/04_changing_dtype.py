# we can change the dtype of the item stored in the array, this feature is very useful in memory management
import numpy as np

# we can also set the datatype at the time of creation
arr = np.array([1, 2, 3, 4, 5], dtype=np.int16)
print(arr)
print(arr.dtype)

# we can also use astype
arr = arr.astype(np.float64)
print(arr)
print(arr.dtype)
