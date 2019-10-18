import matplotlib.pyplot as plt 
import numpy as np 
from numpy import linalg
from matplotlib.patches import Ellipse
from math import atan2

r = 20
L = 12
min = 0.0
max = 5.0
steps = 100
space = (max - min)/steps

t = np.arange(min, max+space, space)

ph1 = 0.25*t*t
ph2 = 0.5*t

th = (r/(2*L))*(ph1-ph2)
x = (r/2)*(ph1+ph2)*np.cos(th)
y = (r/2)*(ph1+ph2)*np.sin(th)

mu, sigma = 0.0, 0.3

xerr = np.random.normal(mu,sigma,x.size)
yerr = np.random.normal(mu,sigma,y.size)

plt.plot(x,y,'b-',xerr+x,yerr+y,'r.')
plt.xlim(-10, 90)
plt.ylim(-20, 80)
plt.show()

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
ell = Ellipse((np.mean(x),np.mean(y)),r1,r2,angle)
#  make the ellipse subplot
a = plt.subplot(111, aspect='equal')
ell.set_alpha(0.1)    #  make the ellipse lighter
a.add_artist(ell)   #  add this to the plot

plt.show()