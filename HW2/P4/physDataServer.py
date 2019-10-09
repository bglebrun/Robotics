import numpy as np 
import zmq
import time

context = zmq.Context()
print("Connecting to the server...")
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://*:5555")

topic = "physData"
btopic = bytes(topic,'ascii')

min = 0.0
max = 10.0
steps = 100.0
space = (max - min)/steps
freq = 5.0 #Hz
t = 1.0/freq

print("Sending data at frequency {} Hz, {} s".format(freq,t))
#send data
for i in np.arange(min, max, space):
    y = 15.0 - i
    print("Sending x: {} y: {}".format(i,y))
    message = bytes(str(i) + " " + str(y),'ascii')
    publisher.send_multipart([btopic, message])
    time.sleep(t)

publisher.close()
context.term()