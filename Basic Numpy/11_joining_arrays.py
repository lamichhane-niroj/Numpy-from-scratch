# we will use concatenate function to join two arrays

import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.concatenate((arr1, arr2))
print(newarr)

# but what about 2D
arr3 = np.array([[2, 4, 6, 8], [1, 3, 5, 7]])
arr4 = np.array([[3, 5, 7, 9], [4, 6, 8, 10]])

# for row axis we put 1 and for column axis we put 0
newarr1 = np.concatenate((arr3, arr4), axis=0)
print(newarr1)

newarr1 = np.concatenate((arr3, arr4), axis=1)
print(newarr1)


# stacking horizontally, vertically, depth
horstack = np.hstack((arr3, arr4))
print(horstack)

verstack = np.vstack((arr3, arr4))
print(verstack)

destack = np.dstack((arr3, arr4))
print(destack)


# column stack and row stack
rowstack = np.row_stack((arr3, arr4))
print(rowstack)

colstack = np.column_stack((arr3, arr4))
print(colstack)

# when will you use it?
# -> If you have data from different source you need to merge it while doing analysis on data
