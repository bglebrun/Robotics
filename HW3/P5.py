import matplotlib.pyplot as plt 
import numpy as np 
from numpy import linalg
from matplotlib.patches import Ellipse
from math import atan2


def ddstep(xc, yc, qc,r,l,dt,w1,w2):
   xn = xc + (r*dt/2.0)*(w1+w2)*np.cos(qc)
   yn = yc + (r*dt/2.0)*(w1+w2)*np.sin(qc)
   qn = qc + (r*dt/(2.0*l))*(w1-w2)
   return (xn,yn,qn)

def wheel_eqn(t):
    ph1 = 0.25*t*t
    ph2 = 0.5*t
    return (ph1,ph2)

r = 20
L = 12
min = 0.0
max = 5.0
steps = 100
dt = (max - min)/steps
xc = yc = thc = 0

t = 0

x = []
y = []
th = []

for i in range(steps):
    ph1c,ph2c=wheel_eqn(t)
    xc, yc, thc = ddstep(xc,yc,thc,r,L,dt,ph1c,ph2c)
    t = t + dt
    x.append(xc)
    y.append(yc)
    th.append(thc)

mu, sigma = 0.0, 0.3

xerr = np.random.normal(mu,sigma,len(x))
yerr = np.random.normal(mu,sigma,len(y))

plt.plot(x,y,'b-',xerr+x,yerr+y,'r.')
plt.xlim(-10, 90)
plt.ylim(-20, 80)
plt.show()

xfinal = x
yfinal = y

f=open("HW3/simulation.txt","w+")
for i in range(100):
    xc = yc = thc = 0
    t = 0

    x = []
    y = []
    th = []

    for i in range(steps):
        ph1c,ph2c=wheel_eqn(t)
        xc, yc, thc = ddstep(xc,yc,thc,r,L,dt,ph1c,ph2c)
        t = t + dt
        x.append(xc)
        y.append(yc)
        th.append(thc)

    xerr = np.random.normal(mu,sigma,len(x))
    yerr = np.random.normal(mu,sigma,len(y))

    for i in range(steps):
        f.write("{},{}\n".format(x[i]+xerr[i],y[i]+yerr[i]))

f.close()

s = 2.447651936039926
#  assume final locations are in x & y
mat = np.array([x,y])
#  find covariance matrix
cmat = np.cov(mat)
# compute eigenvals and eigenvects of covariance
evals, evec = linalg.eigh(cmat)
r1 = 2*s*np.sqrt(evals[0])
r2 = 2*s*np.sqrt(evals[1])
#  find ellipse rotation angle
angle = 180*atan2(evec[0,1],evec[0,0])/np.pi
# create ellipse
ell = Ellipse((np.mean(x),np.mean(y)),width=r1,height=r2,angle=angle)
#  make the ellipse subplot
a = plt.subplot(111, aspect='equal')
ell.set_alpha(0.1)    #  make the ellipse lighter
a.add_artist(ell)   #  add this to the plot
plt.xlim(-50, 150)
plt.ylim(-100, 100)

plt.show()