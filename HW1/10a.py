import math as mt
import numpy as np
import matplotlib.pyplot as plt

a1 = 15.0
a2 = 15.0


def twolinkik(x, y):
    d = (x*x+y*y-a1*a1-a2*a2)/(2*a1*a2)
    t2 = mt.atan2(-mt.sqrt(1.0-d*d), d)
    t1 = mt.atan2(y, x)-mt.atan2(a2*mt.sin(t2), a1+a2*mt.cos(t2))
    return t1, t2


x = np.arange(0.1, 25, 0.1)

x1 = []
y1 = []

for i in x:
    g, h = twolinkik(i, 25-i)
    print(i, 25-i, g, h)
    x1.append(g)
    y1.append(h)

plt.plot(x1)
plt.plot(y1)
plt.title("10a")
plt.show()
