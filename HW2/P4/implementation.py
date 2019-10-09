import numpy as np 
import zmq
import time

context = zmq.Context()
print("Connecting to the server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

min = 0
max = 10
steps = 100
space = (max - min)/steps
freq = 5 #Hz
t = 1/freq*1000

x = np.arange(min, max + steps, steps)
y = 15 - x

while True:
    #send data
    for i in range(steps):
        socket.send(str(i).encode())
        time.sleep(t)