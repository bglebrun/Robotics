import numpy as np
import matplotlib.pyplot as plt
import time
#from math import *

a1 = 15
a2 = 10
step = 0.1

#Setup Arrays
t = np.arange(0, 2*np.pi+step, step)
x = 5*np.cos(t) + 10
y = 5*np.sin(t) + 8

#Compute joint angles and check them
a1 = 15.0
a2 = 10.0
d = (x*x + y*y - a1*a1 - a2*a2)/(2*a1*a2)
t2 = np.arctan2(-np.sqrt(1.0-d*d),d)
t1 = np.arctan2(y,x) - np.arctan2(a2*np.sin(t2),a1+a2*np.cos(t2))
xsim1 = a1*np.cos(t1)
ysim1 = a1*np.sin(t1)
xsim = a2*np.cos(t1+t2) + xsim1
ysim = a2*np.sin(t1+t2) + ysim1

plt.figure(1)
plt.subplot(221)
plt.xlim(0, 20)
plt.ylim(0, 15)
plt.ylabel('Y')
plt.title('Requested Path')
plt.plot(x,y)

plt.subplot(222)
plt.xlabel('Theta1')
plt.ylabel('Theta2')
plt.title('Joint Angles for Path')
plt.plot(t1,t2)

plt.subplot(223)
plt.xlim(0, 20)
plt.ylim(0, 15)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Traversed Path')
plt.plot(xsim,ysim)

plt.ion()  #  Turn on interactive mode
plt.subplot(224)
arm = plt.plot([],[],'b-')  # Create empty plot
plt.xlim(0, 20)
plt.ylim(0, 15)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#Animation
for i in range(t.size):
    x1 = xsim1[i]
    y1 = ysim1[i]
    x2 = xsim[i]
    y2 = ysim[i]
    plt.setp(arm,xdata = [0,x1,x2], ydata = [0,y1,y2])
    plt.draw()
    plt.plot([x2],[y2],'b.')
    time.sleep(0.05)

plt.ioff()
plt.show()