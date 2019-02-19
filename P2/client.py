import socket
from Seq import Seq
# Create a socket for communicating with the server

print('socket created')
port = 8080
IP = "212.128.253.103"

#ask the user for a sequence
while True:
    #ALWAYS ASK THE USEWR FOR THE MESSAGE BEFORE SENDING IT TO THE SERVER, BECAUSE OTHERWISE YOU'RE BLOCKING THE SERVER
    seq = Seq(input('enter your sequence: '))

    reverse = seq.reverse()
    comp = seq.complement()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, port))
    info = '\nComplementary chain: {} \nReverse chain: {}'.format(comp, reverse)
    s.send(info.encode())

