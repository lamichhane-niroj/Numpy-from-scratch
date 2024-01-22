import numpy as np

print(np.__version__)

# what is numpy?
# Numpy is a python module for working with arrays. full form - numerical python

# why do we need to learn numpy?
# numpy is very faster than list because numpy uses concept of arrays, and it is written in c language

# How do you think list work?
# List stores the variable address of the memory in it rather than the variable itself
# whereas array stores in consecutive location in memory so array is fast because it can access data easily but list
# first go to the address and fetch the data

# lets make a comparison

# 1. space comparison
mylist1 = [i for i in range(10000000)]
arr = np.arange(10000000)

import sys

print("Size used by list: ",sys.getsizeof(mylist1),"bytes")
print("Size used by numpy array: ",sys.getsizeof(arr),"bytes")

# we see that the size by numpy array is about half, we can also change the dtype of array but not list

# 2. Time comparsion
import time

# list operation
mylist1 = [i for i in range(10000000)]
mylist2 = [i for i in range(10000000, 20000000)]
arr = np.arange(10000000)

mylist3 = []

start = time.time()
for i in range(10000000):
    mylist3.append(mylist1[i] + mylist2[i])

print("Time taken by list:", time.time() - start, "seconds")


# numpy operation
arr1 = np.arange(10000000)
arr2 = np.arange(10000000, 20000000)

start = time.time()
arr3 = arr1 + arr2
print("Time taken by numpy array:", time.time() - start, "seconds")

# we see that the time taken by the numpy array is almost 50 times faster than list


# 3. syntax comparison
# Above code shows how simple is to use numpy
