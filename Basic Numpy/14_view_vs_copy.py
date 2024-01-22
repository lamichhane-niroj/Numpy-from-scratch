# changes will be reflected if we edit in view mode but not in copy mode

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# assignment operator and slicing also does the view or shallow copy so modifying it will affect the original array
arr1 = arr.view()
arr2 = arr.copy()

# view or shallow copy
print(arr1 is arr)
print(arr1.base is arr)

# copy or deep copy
print(arr2 is arr)
print(arr2.base is arr)
print(arr)
print(arr1)
print(arr2)

arr1[0] = 5
arr2[1] = 10

print(arr)
print(arr1)
print(arr2)
