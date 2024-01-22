# We will study matplotlib after completing pandas, we can take a look for now
import numpy as np
import matplotlib.pyplot as plt

# plotting the straight line x = y
x = np.linspace(-10, 10, 100)
y = x

plt.plot(x, y)
plt.show()

# plotting parabola
x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)
plt.show()

# plotting sine curve
x = np.linspace(-10, 10, 200)
y = np.sin(x)

plt.plot(x, y)
plt.show()

# plotting exponential
x = np.linspace(-10, 10, 100)
y = np.exp(x)

plt.plot(x, y)
plt.show()

# plotting logarithm
x = np.linspace(0.2, 1, 100)
y = np.log(x)

plt.plot(x, y)
plt.show()
