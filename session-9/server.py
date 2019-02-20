import socket
import termcolor
import sys

PORT = 8080
IP = '212.128.253.112'
MAX_open_request = 5


def process_client(cs):
    # reciving the message
    msg = cs.recv(2048).decode('utf-8')
    if msg == 'EXIT':
        sys.exit(0)
    else:
        termcolor.cprint(msg, 'blue')

    cs.close()


# create a socket to connect to the client
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((IP, PORT))

server_socket.listen( (MAX_open_request))

print('socket ready: {}'.format(server_socket))

while True:
    print('waiting for connections at : {}, {}'.format(IP, PORT))

    # .accept() blocks the progran until a client connects
    (client_socket, address) = server_socket.accept()

    # ... process the client's request
    process_client(client_socket)
