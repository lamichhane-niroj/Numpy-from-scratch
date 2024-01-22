# Advance Indexing
# 1. Fancy Indexing
# 2. Boolean Indexing

# Fancy Indexing
# We know only some pattern element can be achieved using normal indexing. so we need advanced indexing to access any element
import numpy as np

a = np.random.randint(1, 100, (5, 4))
print(a)
'''
[[96 36 29 57]
 [65 72 69 59]
 [24 91 90 61]
 [33 75 87 38]
 [17 83 78  7]]
'''
# suppose we need 0,1,4 row element. For this we use fancy indexing
print(a[[0, 1, 4]])

# suppose we need 36, 90, 75, 7
print(a[[0, 2, 3, 4], [1, 2, 1, 3]])

# suppose we need 2nd and 3rd row
print(a[[2, 3], :])

# Boolean indexing
# it acts like masking or filtering
b = np.random.randint(1, 101, (5, 5))

# Now we need to get only even number -> use boolean indexing
print(b[b%2 == 0])

# find elements that are greater than 50 and are even
print(b[(b % 2 == 0) & (b > 50)])
