# i for integer
# f for float
# b for boolean
# u for unsigned integer
# c for complex float
# m for timedelta
# M for datetime
# O for object
# S for string
# U for unicode string
# V for memory
import numpy as np

# checking the datatype
arri = np.array([1, 2, 3, 4])
print(arri.dtype)

arrf = np.array([1.1, 2.2])
print(arrf.dtype)

arrb = np.array([True, False])
print(arrb.dtype)

arrs = np.array(["apple", "ball"])
print(arrs.dtype)

arro = np.array([1.2, True])
print(arro.dtype)


# derived datatype
arr1 = np.array([1, 2, 3, 4], dtype='S')
print(arr1.dtype)
print(arr1)

arr2 = np.array([1.1, 0], dtype='f')
print(arr2.dtype)
print(arr2)

# we can specify also the bytes for the values to store
arr3 = np.array([1, 2, 3, 4, 5], dtype='i4')
print(arr3)
print(arr3.dtype)

# converting using astype function
arr3 = arr3.astype('f')
arr3 = arr3.astype(int)
print(arr3)
