import numpy as np

arr = np.array((1, 2, 3, 4, 5))
print(arr[0])

arr1 = np.array([[1, 2, 3], [5, 6, 7]])
print(arr1[0, 0])
print(arr1[0][0])

arr2 = np.array([[1, 2, 3], [5, 6, 7]], ndmin=3)
print(arr2)
print(arr2[0, 0, 0])
print(arr2[0][0])

arr3 = np.array([[[1, 2, 3]], [[4, 5, 6]]])
print(arr3[0, 0, 1])

print(np.arange(10000))

# it shows that numpy doesn't print all the array, to enable it we should use
import sys

np.set_printoptions(threshold=sys.maxsize)
print(np.arange(1, 10001).reshape(100, 100))


