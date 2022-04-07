import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(0, 5)   # [0 1 2 3 4]
# y = x ** 2            # [0 1 4 9 16]
x = np.linspace(-10,10,100)
# y = x**2
y = np.sin(x)   # -1~1

plt.plot(x, y)
plt.show()