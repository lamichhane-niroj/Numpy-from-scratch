import numpy as np

# for integers we use random.randint()
num1 = np.random.randint(100)
print(num1)

# for floating number we use random.rand() which gives random real number between 0 and 1
num2 = np.random.rand()
print(num2)

# creation of 1d array of random integers
arr1 = np.random.randint(0, 100, size=5)
print(arr1)

# creation of 2d array of random float
arr2 = np.random.rand(3, 3)
print(arr2)

# choice method - it randomly choose a element from the array
arr3 = np.array([1, 2, 4, 6, 7, 9, 0])
print(np.random.choice(arr3))

# we can also create a multidimensional array based on the random value choosen from a 1D array
arr4 = np.array([2, 4, 3, 1, 5, 8, 9, 0, 6])
print(np.random.choice(arr4, size=(3, 5)))

# shuffle method
arr1 = np.array([1, 3, 5, 6, 7, 9])
np.random.shuffle(arr1)
print(arr1)

# permutation method
arr2 = np.array([2, 4, 6, 8, 0])
print(np.random.permutation(arr2))

# sort function
arr1 = np.array([1, 2, 7, 3, 9, 4, 5])
print(np.sort(arr1))

arr2 = np.array(["apple", "cat", "banana"])
print(np.sort(arr2))
