import numpy as np
from numpy.linalg import linalg
import matplotlib.pyplot as plt

k = 1
F = np.array([[0, 0.1], [-0.02, 0.2]])
GkUk = np.array([[0], [2 * np.sin(k / 25)]])
H = np.array([[1,0]])
HT = np.array([[1],[0]])
V = np.array([[0.0025, 0], [0, 0.0025]])
W = 0.0625
x0 = np.array([[0.025],[0.1]])
p0 = np.array([[0,0],[0,0]])

#Generate Z data first via hint on problem
#Create a matrix Z to hold all x values with just the control input
Z = []
Z.append(x0)
#populate the Z matrix for use in calculations
while (k<100):
    G = np.array([[0], [2 * np.sin((k/25))]])
    newZ = Z[k-1] + G
    Z.append(newZ)
    #print(newZ)
    k = k+1

#reset k
k = 1

prevX = x0
prevP = p0
x = []
y = []

X = [x0]
P = []

while (k<100):

    x_process_update = np.dot(F,X[k-1]) + GkUk
    P_variance_update = np.dot(F,np.dot(prevP,np.transpose(F))) + V
    innovation = Z[k] - np.dot(H,x_process_update)
    Innovation_covariance = np.dot(H,np.dot(P_variance_update,HT)) + W
    Kal_gain = np.dot(np.dot(P_variance_update,HT), linalg.inv(Innovation_covariance))
    X.append(x_process_update + (Kal_gain * innovation))
    P.append(P_variance_update - Kal_gain*np.dot(H,P_variance_update ))
    tempX = X[k-1]
    x.append(tempX[0])
    y.append(tempX[1])
    k = k+1

plt.plot(x,y)
plt.show()