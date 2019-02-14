import socket
from Seq import Seq
# Create a socket for communicating with the server

print('socket created')
port = 8081
IP = "192.168.0.15"

while True:
    #ask the user for a sequence
    seq = input('enter your sequence: ')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, port))

    #send it
    s.send(seq.encode())

    #receive the complementary sequence
    comp=s.recv(2048).decode('utf-8')
    print(comp)

    s.close()