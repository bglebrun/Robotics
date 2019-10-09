import zmq

context = zmq.Context()
print("Connecting to the chat server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

user_name = input('Welcome to the chat client, Enter name: ')

socket.send_string('New user {} has entered the channel'.format(user_name))
# print("Type /help for commands")

while True:
    message = socket.recv_string()
    print(message)

    message_string = input('Channel: ')
    send_message = user_name + ":" + message_string
    socket.send_string(send_message)