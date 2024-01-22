# creating of ndarray in numpy
# numpy array is the collection of homogeneous object. so the datatype for element must be same
import numpy as np

# array can be created in numpy using different methods

# 1 D arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# any iterable object can be passed inside it
arr2 = np.array((1.2, 2, 3, 4, 5))
print(arr2)

arr4 = np.array(['1', '2', '3'])
print(arr4)

# 2D arrays
arr5 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr5)

# some other method for creating array in numpy
zarr = np.zeros((2, 3))
print(zarr)

zlarr = np.zeros_like(zarr)
print(zlarr)

oarr = np.ones((5, 3))
print(oarr)

olarr = np.ones_like(zarr)
print(olarr)

# it gives random value
earr = np.empty((4, 4), dtype=int)
print(earr)

elarr = np.empty_like(oarr)
print(elarr)

# it works like python range
arang = np.arange(1, 10, 0.5)
print(arang)

# when the number is fixed but gap is not fixed
lins = np.linspace(1, 10, 20)
print(lins)

# using random - gives random float between 0 and 1
rand = np.random.random((2, 3))
print(rand)

# using identity or eye - returns identity array
iden = np.identity(5)
print(iden)

def func(x, y):
    return x*2 + y


ff = np.fromfunction(func, (3, 2))
print(ff)

# where to use ones and zeros array?
# -> To initialize the array



