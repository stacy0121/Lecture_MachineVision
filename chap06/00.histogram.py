import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(0, 8, 9)
print(a)

bins = np.linspace(0, 8, 9)

plt.hist([a], bins, label=['a'])
plt.legend(loc='upper left')
plt.show()