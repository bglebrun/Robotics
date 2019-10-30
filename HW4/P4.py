import numpy as np 
from scipy.signal import argrelmax, argrelmin

steps = 100.0

v1min = 0.18
v1max = 0.22
v1space = (v1max - v1min)/steps

v2min = 0.27
v2max = 0.33
v2space = (v2max-v2min)/steps

f = 0.7
b = 10.0

v1 = np.arange(v1min, v1max, v1space, np.float)
v2 = np.arange(v2min, v2max, v2space, np.float)

g = (f*b)/(v1+v2)

print("g: ", g)

print("max: ", argrelmax(g))
print("min: ", argrelmin(g))