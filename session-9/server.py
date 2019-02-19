import socket

PORT = 8080
IP = '212.128.253.93'
MAX_open_request = 5


def process_client(cs):
    # reciving the message
    msg = cs.recv(2048).decode('utf-8')
    # printing it
    print('Message form the client: {}'.format(msg))
    # sending it back, because we are an echo server
    cs.send(str.encode(msg))

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
