import math as mt
import numpy as np
import matplotlib.pyplot as plt

a1 = 15.0
a2 = 15.0


def forward_k_two_link(t1, t2):
    x1 = a2*mt.cos(t1+t2) + a1*mt.cos(t1)
    y1 = a2*mt.sin(t1+t2)+a1*mt.sin(t1)
    return x1, y1


def inverse_k_two_link(x, y):
    d = (x*x+y*y-a1*a1-a2*a2)/(2*a1*a2)
    t2 = mt.atan2(-mt.sqrt(1.0-d*d), d)
    t1 = mt.atan2(y, x)-mt.atan2(a2*mt.sin(t2), a1+a2*mt.cos(t2))
    return t1, t2


# From problem 10
x = np.arange(0.1, 25, 0.1)
t = np.arange(0, mt.pi, 0.1)

# From square problem
sqx = [5,5,20,20,5]
sqy = [0,15,15,0,0]

# Theta values for our solutions
xt1 = []
yt1 = []

xt2 = []
yt2 = []

sqtx = []
sqty = []

# Find theta values for x + y = 25
for i in x:
    g, h = inverse_k_two_link(i, 25-i)
    xt1.append(g)
    yt1.append(h)

# Find theta values for 0 <= t < pi
for i in t:
    j = 10*mt.cos(i)+15
    k = 10*mt.sin(i)
    g, h = inverse_k_two_link(j, k)
    xt2.append(g)
    yt2.append(h)

for i in range(0, len(sqx)):
    l, m = inverse_k_two_link(sqx[i], sqy[i])
    sqtx.append(l)
    sqty.append(m)


# Results
x1 = []
y1 = []

x2 = []
y2 = []

sqrx = []
sqry = []

for i in range(0, max(len(xt1), len(yt1))):
    g, h = forward_k_two_link(xt1[i], yt1[i])
    x1.append(g)
    y1.append(h)

for i in range(0, max(len(xt2), len(yt2))):
    j, k = forward_k_two_link(xt2[i], yt2[i])
    x2.append(j)
    y2.append(k)

for i in range(0, max(len(sqtx), len(sqty))):
    l, m = forward_k_two_link(sqtx[i], sqty[i])
    sqrx.append(l)
    sqry.append(m)


plt.plot(x1, y1)
plt.show()

plt.plot(x2, y2)
plt.show()

plt.plot(sqrx, sqry)
plt.show()