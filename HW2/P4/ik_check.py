import zmq
import time
import math as mt
import matplotlib.pyplot as plt

context = zmq.Context()

print("Connecting to physData server")
physSub = context.socket(zmq.SUB)
physSub.connect("tcp://localhost:5555")

print("Connecting to IK server")
ikSub = context.socket(zmq.SUB)
ikSub.connect("tcp://localhost:5556")

physTopic = "physData"
physSub.setsockopt_string(zmq.SUBSCRIBE, physTopic)

ikTopic = "thetaData"
ikSub.setsockopt_string(zmq.SUBSCRIBE, ikTopic)

a1 = 10
a2 = 10

freq = 5.0 #Hz
t = 1.0/freq

def forward_k_two_link(t1, t2):
    x1 = a2*mt.cos(t1+t2) + a1*mt.cos(t1)
    y1 = a2*mt.sin(t1+t2)+a1*mt.sin(t1)
    return x1, y1

xa = []
ya = []

t1a = []
t2a = []

while len(xa)!=98:
    time.sleep(t)
    [paddress,pmessage] = physSub.recv_multipart()
    [taddress,tmessage] = ikSub.recv_multipart()
    
    tvect = tmessage.split(b" ")
    t1 = eval(tvect[0])
    t2 = eval(tvect[1])

    pvect = pmessage.split(b" ")
    x1 = eval(pvect[0])
    y1 = eval(pvect[1])

    print("x:{} y:{} t1:{} t2:{}".format(x1,y1,t1,t2))

    xa.append(x1)
    ya.append(y1)

    t1a.append(t1)
    t2a.append(t2)

xb = []
yb = []

for i in range(min(len(t1a), len(t2a))):
    g, h = forward_k_two_link(t1a[i], t2a[i])
    xb.append(g)
    yb.append(h)

print("Plotting...")
plt.figure(1)

plt.subplot(221)
plt.xlim(0,20)
plt.ylim(0,15)
plt.ylabel('Y')
plt.xlabel('X')
plt.title('PhysData Original')
plt.plot(xa,ya, 'g-')

plt.subplot(222)
plt.xlim(0,20)
plt.ylim(0,15)
plt.ylabel('Y')
plt.xlabel('X')
plt.title('Forward Kinematic results')
plt.plot(xb,yb, 'b-')

plt.show()