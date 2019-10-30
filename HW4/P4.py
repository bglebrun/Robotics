import numpy as np 

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

actual = (f*b)/(0.2+0.3)

print("g: ", g)

maxval = np.amax(g)
minval = np.amin(g)

print("max: ", maxval)
print("min: ", minval)
print("max percent error: ", abs((maxval-actual)/actual) * 100 )
print("min percent error: ", abs((minval-actual)/actual) * 100 )