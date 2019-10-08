import zmq

context = zmq.Context()
print("Connecting to the chat server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def help():
    print("/help: show this prompt\n/shutdown close the server")
    print("/exit: disconnect chat client from server")

user_name = input('Welcome to the chat client, enter name: ')

socket.send_string('New user {} has entered the channel'.format(user_name))

message_name = '{}'.format(user_name)
while True:
    message_string = input('Channel: ')

    if message_string == '/help':
        help()
    elif message_string == '/exit':
        socket.send_string('User {} has left the chat.'.format(user_name))
        print("Disconnecting")
        break
    elif message_string == '/shutdown':
        socket.send_string('Shutting down server')
        print("Disconnecting")
        break
    else:
        socket.send_string(message_name + message_string)

    message = socket.recv_string()