import matplotlib.pyplot as plt 
import numpy as np 

L1 = 0.3
L2 = 0.2
r = 0.08

min = 0.0
max = 10.0
steps = 100.0
space = (max - min)/steps

t = np.arange(0, 10, 0.05)

th1 = 0.75*np.cos(t/3.0)
th2 = 1.5*np.cos(t/30)
th3 = -1.0
th4 = 0.5

A = (th1+th2+th3+th4)
B = (-1*th1+th2+th3-th4)
C = (th2-th1-th3+th4)

th = r*t/4*(C/(L1+L2))
x = r*t/4*(A*np.cos(th)-B*np.sin(th))
y = r*t/4*(A*np.sin(th)+B*np.cos(th))

s = 0.075
u = s*np.cos(th)
v = s*np.sin(th)

plt.plot(x,y,'b.')
plt.show()

plt.quiver(x,y,u,v,scale=s,units='xy',color='g')
# plt.savefig('mecanumpath.pdf')
plt.show()