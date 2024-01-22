import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

for item in arr:
    print(item)

print()

# nditer first flattens the array and returns iterator for the array. so we access each item of array
for item in np.nditer(arr):
    print(item)

arr2 = np.array([[5, 6, 7, 9], [4, 6, 7, 8]])

print()
for a in arr2:
    for b in a:
        print(b)

print()
for item in np.nditer(arr2):
    print(item)
