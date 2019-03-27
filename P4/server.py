import socket
import termcolor

# Change this IP to yours!!!!!
IP = "212.128.253.108"
PORT = 8023
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    if msg != '':
        print()
        print("Request message: \n{}".format(msg))

        # getting the server the client wants to access
        request = msg.partition('\n')[0].split(' ')[1]

        # answering the user depending on his request
        if request == '/':
            with open('index.html', 'r') as f:
                content = f.read()

        elif request == '/blue':
            with open('blue.html', 'r') as f:
                content = f.read()

        elif request == '/pink':
            with open('pink.html', 'r') as f:
                content = f.read()

        else:
            with open('error.html', 'r') as f:
                content = f.read()

        # response message
        status_line = 'HTTP/1.1 200 OK\r\n'

        header = 'Content-type: text/HTML\r\n'

        header += 'Content-lenght: {}\r\n'.format(len(str.encode(content)))

        reponse_message = status_line + header + '\r\n' + content

        cs.send(str.encode(reponse_message))

    # in case there's an empty request message
    else:
        print('empty request message!!')

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind(('', PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)
