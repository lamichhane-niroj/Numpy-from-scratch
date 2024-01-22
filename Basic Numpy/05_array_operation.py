# Scalar operation and Vector operation
# Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.

import numpy as np

# scalar operation +, -, *, /, %, **, //
a = np.arange(1,10).reshape(3,3)
print(a*2)
print(a+2)
print(a**2)

# relational operation >, <, >=, <=, ==, !=
print(a>=2)

# vector operation - shape must be same
# simple arithmetic operation
a = np.array([5.2, 3.5, 4.5, 9.2])
b = np.arange(4)

c = a - b
d = a + b
e = a * b
print(c)
print(d)
print(e)

# * does the operation element wise for matrix product use @ or dot
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)
print(A.dot(B))

# Some operations, such as += and *=, act in place to modify an existing array rather than create a new one.
A += B
print(A)

B += 3
print(B)

B *= 2
print(B)

# what if they have different datatypes
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.linspace(2, 3, 4)
arr2.shape = (2, 2)

arr2 += arr1  # it will work fine
# arr1 += arr2  # but this will generate error

# some useful unary operation of ndarray
print(arr1.sum())
print(arr1.min())
print(arr1.max())

