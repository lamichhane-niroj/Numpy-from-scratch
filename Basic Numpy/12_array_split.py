import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr1, 3)

newarr1 = np.array_split(arr1, 4)
print(newarr1)

# what about 2D arrays?
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
newarr2 = np.array_split(arr2, 3)
print(newarr2)

# using axis
arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
newarr3 = np.array_split(arr2, 3, axis=1)
print(newarr3)

# using specific method
# hsplit
arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
newarr4 = np.hsplit(arr2, 3)
print(newarr4)

# vsplit
arr5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
newarr5 = np.vsplit(arr5, 3)
print(newarr5)

# Split `a` after the first and the second column
print(np.hsplit(arr5, (1, 2)))
