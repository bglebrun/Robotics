import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Server started")
while True:
    message = socket.recv_string()
    print("%s" % message)
    socket.send_string(message)
    if message == 'Shutting down server':
        break
    time.sleep(1)