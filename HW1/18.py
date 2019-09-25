import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(5, 15)
y = 8.0+(25.0-(x-10.0)**2.0)**0.5

plt.title("18")
plt.plot(x, y)
plt.plot(x, np.linspace(1, 1, len(x))*8)
plt.show()
