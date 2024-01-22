import numpy as np

# We can put axis in all the below function for operating in row or column

# sort function
a = np.random.randint(1, 100, (20,))
print(np.sort(a))

# axis 1 for row and 0 for column
b = np.random.randint(1, 100, (6, 4))
print(np.sort(b, axis=1))
print(np.sort(b, axis=0))

# append function
print(np.append(a, [20, 30, 40]))
print(np.append(b, np.ones((6, 1)), axis=1))

# unique function
print(np.unique(a))

# expand_dims
print(np.expand_dims(a, axis=0))

# argmax
print(np.argmax(a))

# argmin
print(np.argmin(a))

# cumsum
print(np.cumsum(a))

# cumprod
print(np.cumprod(a))

# percentile
print(np.percentile(a, 25))  # 25 percent data are below this number and 75 percent is above the number

# histogram -> It gives the frequency count of given interval (bins)
c = np.random.randint(1, 100, (20, ))
print(c)
print(np.histogram(c, bins=[0, 20, 40, 60, 80, 100]))

# correlation coefficient
salary = np.array([10000, 20000, 30000, 40000, 50000])
experience = np.array([1.5, 2.5, 3.5, 4.5, 2])

print(np.corrcoef(salary, experience))

# isin
values = [1, 5, 7, 3]
arr = np.arange(1, 25)
print(np.isin(arr, values))

# flip
print(np.flip(arr))

# put
np.put(arr, [0, 1], [55, 77])
print(arr)

# delete
print(np.delete(arr, [0, 3, 5]))

# set functions
print(np.intersect1d(arr, a))
print(np.union1d(arr, a))
print(np.setdiff1d(arr, a))
print(np.setxor1d(arr, a))
print(np.in1d(arr, 5))

# clip
print(np.clip(arr, a_min=10, a_max=20))
