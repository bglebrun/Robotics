import numpy as np 
from scipy.signal import argrelextrema

f = 0.7
b = 10.0

v1 = np.arange(0.18, 0.22, 0.001, np.float)
v2 = np.arange(0.27, 0.33, 0.001, np.float)

g = (f*b)/(v1+v2)

print("max: ", argrelextrema(g, np.greater))
print("min: ", argrelextrema(g, np.less))