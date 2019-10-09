import zmq
import time
import math as mt

context = zmq.Context()

# Create the subscriber process
print("Connecting to physDataServer")
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://localhost:5555")

# Create the thetaData server
print("Creating thetaData server")
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://*:5556")

topicPub = "thetaData"
btopicPub = bytes(topicPub,'ascii')

topicSub = "physData"
subscriber.setsockopt_string(zmq.SUBSCRIBE, topicSub)

a1 = 10
a2 = 10

freq = 5.0 #Hz
t = 1.0/freq

def twolinkik(x, y):
    d = (x*x+y*y-a1*a1-a2*a2)/(2*a1*a2)
    t2 = mt.atan2(-mt.sqrt(1.0-d*d), d)
    t1 = mt.atan2(y, x)-mt.atan2(a2*mt.sin(t2), a1+a2*mt.cos(t2))
    return t1, t2

while True:
    time.sleep(t)
    [address, message] = subscriber.recv_multipart()
    vect = message.split(b" ")
    x = eval(vect[0])
    y = eval(vect[1])

    t1, t2 = twolinkik(x, y)

    print("Got {}. Angles - t1: {} t2: {}".format(address.decode('ascii'), t1, t2))
    message = bytes(str(t1) + " " + str(t2),'ascii')
    publisher.send_multipart([btopicPub, message])

publisher.close()
subscriber.close()
context.term()