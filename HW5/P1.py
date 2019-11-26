import numpy as np
import matplotlib.pyplot as plt 
from math import atan2, sqrt, sin, cos

r = 2.0 * 0.01
l = 5.0 * 0.01
dia = 10 * 0.01
dt  = 0.01
Tend = 10000.0
N = int(Tend/dt)

v = 1.0
k1 = 2.0
k2 = 5.0

x = np.zeros(N)
y = np.zeros(N)
th = np.zeros(N)


xpts = [0,1,2,3,4,5,4,3,2,1,0,0]
ypts = [0,1,0,-1,0,1,2,3,3,2,1,0]

list_index = 1
i= 0

print(len(xpts))
while(list_index<len(xpts) or list_index<len(ypts)):
    print("working on", xpts[list_index],ypts[list_index])
    while (i < N-1):
        th_err = atan2(ypts[list_index] - y[i], xpts[list_index] - x[i]) - th[i]
        d1 = abs(x[i] - xpts[list_index])
        d2 = abs(y[i] - ypts[list_index])
        w = v
        d = sqrt(d1*d1+d2*d2)
        if (d<=dia):
            break
        w1 = w + k1 * th_err
        w2 = w - k1 * th_err
        if (d<5):
            w1, w2 = k2*d*(w + k1*th_err), k2*d*(w - k1*th_err)
        dx = (r*dt/2.0)*(w1+w2)*cos(th[i])
        dy = (r*dt/2.0)*(w1+w2)*sin(th[i])
        dth = (r*dt/(2.0*l))*(w1-w2)
        x[i+1] = x[i] + dx
        y[i+1] = y[i] + dy
        th[i+1] = th[i] + dth
        i = i+1

    list_index=list_index+1

plt.plot(x,y)
plt.scatter(xpts,ypts)
plt.show()