# shape of the array is the number of rows and column of an array
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# now lets change the shape of an array using ndmin
arr1 = np.array([0, 0, 0, 1], ndmin=3)
print(arr1.shape)

# ravel function returns by flattening the array
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(arr2)
arr2 = arr2.ravel()
print(arr2)

# reshape returns the new array whereas resize changes the original array
print(arr.reshape(4, 2))
arr.resize((4, 2))

# transpose of array
arr3 = np.array([[1, 2], [3, 4]])
print(np.transpose(arr3))
print(arr3.T)
print(arr3.T.shape)

arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# if you don't know the dimension you can put -1 to say calculate it yourself but only one dimension can be put to -1

print(arr4.reshape((3, 4)))
print(arr4.reshape((3, 2, -1)))

