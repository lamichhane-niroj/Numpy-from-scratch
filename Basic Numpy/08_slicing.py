import numpy as np

# all python slicing concepts are used here
arr = np.array([1, 2, 3, 4, 5])

arr1 = arr[:3]
arr2 = arr[3:]

arr1[0] = 5
arr2[0] = 7

# slicing of array creates view so changes in slicing reflects on original array

print(arr)
print(arr1)
print(arr2)

# slicing of 2d arrays
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print 8 9 10
arr3 = arr2[1][2:]
print(arr3)
print(arr2[1, 2:])

# print 5 and 10
print(arr2[0:2, 4])

# print 4 5 and 9 10
print(arr2[0:2, 3:5])

arr3 = np.linspace(1, 10, 10)
arr3[0:6:2] = 1000
print(arr3)

# : can be replaced with ...
newarr = np.linspace(1, 100, 100).reshape(10, 10)
print(newarr)

print(newarr[0:5, ...])
# is equal to
print(newarr[0:5, :])


# slicing of 3D array
c = np.arange(18).reshape((3, 2, 3))
print(c)
# [[[ 0  1  2]
#   [ 3  4  5]]
#
#  [[ 6  7  8]
#   [ 9 10 11]]
#
#  [[12 13 14]
#   [15 16 17]]]

# get the element 2, 8, 14
print(c[:, 0::2, 2])

# get the element 0 2, 12 14
print(c[::2, ::2, ::2])

# get the element 3 4 5, 9 10 11, 15 16 17
print(c[:, 1, ...])

