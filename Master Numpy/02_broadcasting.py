# Broadcasting describes how NumPy treats arrays with different shapes during arithmetic operation
# The smaller array is broadcast across the larger array to have a compatible shape

# rules of broadcasting
# 1. make two array have the same dimension
# -> Add 1 to the head of lower dimension
# 2. make each dimension of array the same size
# -> increase the 1 to the required shape
# -> if there is no one then it will throw error

import numpy as np

a = np.arange(1, 21).reshape((4, 5))
b = np.linspace(20, 24, 4, dtype='i8').reshape((4, 1))

print(a)
print(b)

print(a + b)

c = np.arange(16).reshape((4, 4))
d = np.arange(4).reshape((2, 2))

# print(c + d) # This will raise an error
