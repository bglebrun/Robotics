import numpy as np 
import zmq
import time
import csv

context = zmq.Context()
print("Creating server...")
pubVel = context.socket(zmq.PUB)
pubVel.bind("tcp://*:5555")

pubAct = context.socket(zmq.PUB)
pubAct.bind("tcp://*:5556")

velTopic = "WheelVel"
bVelTopic = bytes(velTopic,'ascii')

pubTopic = "Active"
bPubTopic = bytes(velTopic, 'ascii')

min = 0.0
max = 10.0
steps = 100.0
space = (max - min)/steps
freq = 10.0 #Hz
t = 1.0/freq

active = 1

theta = np.empty((0,2), np.float32)

for i in np.arange(min, max+space,space):
    t1 = 2.0 + 2.0*np.exp(i*-1)
    t2 = 2.0 + np.exp(-2.0*i)
    theta = np.append(theta, np.array([[t1,t2]]), axis=0)

print("Printing X")
print(theta)

for i in range(int(max)):
    message = bytes(str(theta[i][1]) + " " + str(theta[i][2]), 'ascii')
    pubVel.send_multipart([bVelTopic, message])
    actMessage = bytes(str(active))
    pubAct.send_multipart([bPubTopic, actMessage])
    time.sleep(t)
    if i == 10:
        active = 0
    
for i in range(5):
    actMessage = bytes(str(active))
    pubAct.send_multipart([bPubTopic, actMessage])
    time.sleep(t)

pubAct.close()
pubVel.close()
context.term()

