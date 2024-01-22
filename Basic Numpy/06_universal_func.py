# ufuncs - universal function
# NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, these are called “universal functions” (ufunc).
# Within NumPy, these functions operate elementwise on an array, producing an array as output.
import numpy as np

# ************************* max, min, sum, product ******************************************
# in 1D array
a = np.random.randint(0, 100, (10,), )
# print(a)

# max element of array
print(np.max(a))
print(a.max())

# min element of array
print(np.min(a))

# sum of elements
print(np.sum(a))

# prod of elements
print(np.prod(a))

# in 2D array
b = np.arange(12).reshape(3, 4)
print(b)

print(np.min(b))

# we can specify axis 0 -> col, 1 -> row
print(np.min(b, axis=1))
print(np.max(b, axis=0))
print(np.sum(b, axis=0))
print(np.prod(b, axis=1))

# ************************* mean, median, standard deviation, variance **********************

print(np.mean(a))
print(np.mean(b, axis=0))
print(np.median(a))
print(np.median(b, axis=1))
print(np.std(a))
print(np.std(b, axis=0))
print(np.var(a))
print(np.var(b, axis=1))
print()

# ************************************ Trignometry, expo, log ***************************
D = np.arange(10)
D = np.exp(D)
print(D)

E = np.arange(10)
E = np.sin(E)
print(E)
#
res = np.add(D, E)
print(res)

print(np.log(a))


# ********************************** Round, ceil, floor **********************************
arr = np.random.random((3, 2)) * 20
print(arr)

print(np.round(arr))
print(np.ceil(arr))
print(np.floor(arr))
