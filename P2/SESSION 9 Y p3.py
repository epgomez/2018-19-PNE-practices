p3

import socket
from Seq import Seq

PORT = 8080
IP = '212.128.253.93'
MAX_CLIENTS = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen( (MAX_CLIENTS))

print('waiting for connections at : {}, {}'.format(IP, PORT))

def letters(ms):
    for i in ms:
        if not (i=='A' or i=='C' or i=='T' or i == 'G'):
            return True
        else:
            return False


def info(s):
    msg = s.recv(2048).decode('utf-8')
    msg = msg.partition('\n')
    seq = msg[0].upper()
    seq = Seq(seq)
    ops = msg[2].split('\n')

    if msg[0] == '':
        return 'ALIVE', seq, ops

    elif letters(msg[0]):
        return 'ERROR', seq, ops
    else:
        return 'OK', seq, ops


def operations (s):
    result, seq, ops = info(s)
    methods_name = ['len', 'complement', 'reverse', 'countA', 'countC', 'countT', 'countG', 'percA', 'percC', 'percT',
                    'percG']
    methods = [seq.len(), seq.complement(), seq.reverse(), seq.count('A'), seq.count('C'), seq.count('T'),
               seq.count('G'), seq.perc('A'), seq.perc('C'), seq.perc('T'), seq.perc('G')]
    count= [1,2,3,4,5,6,7,8,9,10,11]
    info = ''
    for i in op:
        for name, ops, num in zip (methods_name, methods, count):
            if i == name:
                info += methods[num] + '\n'
    return info




while True:
    (client_socket, address) = s.accept()


#SESSION 9

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



