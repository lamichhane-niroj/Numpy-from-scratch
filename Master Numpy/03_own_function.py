# what if we want to use our own mathematical formula and no function exists for that
# sigmoid s(x) = 1 / (1 + e^-x)
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


arr = np.arange(10)
print(sigmoid(arr))

# mean square error
def mse(actual, predicted):
    return np.mean((actual - predicted)**2)


actual = np.random.randint(1, 50, 25)
predicted = np.random.randint(1, 50, 25)

print(mse(actual, predicted))

