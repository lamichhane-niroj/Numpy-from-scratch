import numpy as np

arr = np.array([1, 2, 3, 4, 4, 5, 6, 4, 7, 8])
index = np.where(arr == 4)

print(index)

# find all the index of even element
index = np.where(arr % 2 == 0, arr, 0)
print(index)

# searchSorted - it does binary searching
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
index = np.searchsorted(arr1, 7)
print(index)

# we can also get the index of element to insert in sorted list
arr2 = np.array([2, 4, 6, 8])
index = np.searchsorted(arr2, [1, 3, 5])
print(index)
