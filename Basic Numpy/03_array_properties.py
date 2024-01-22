import numpy as np

arr1 = np.arange(20)

# for 1D array -> 1D array is called vector
# type - ndarray
print(type(arr1))

# datatype of array element
print(arr1.dtype)

# shape of array -> element in each dimension
print(arr1.shape)

# memory used by each item
print(arr1.itemsize)

# number of element in array -> multiplication of shape
print(arr1.size)

# dimension
print(arr1.ndim)


# for 2d array - 2D array is called matrix
arr2 = np.arange(12).reshape((3, 4))

print(type(arr2))

print(arr2.dtype)

print(arr2.shape)

print(arr2.itemsize)

print(arr2.size)

print(arr2.ndim)


# for 3D array - 3D array is called tensor
arr3 = np.arange(12).reshape((2, 3, 2))

print(type(arr3))

print(arr3.dtype)

print(arr3.shape)

print(arr3.itemsize)

print(arr3.size)

print(arr3.ndim)
