import socket
from Seq import Seq

PORT = 8081
IP = '192.168.0.15'
MAX_CLIENTS = 5




def letters(ms):
    for i in ms.upper():
        if not (i == 'A' or i == 'C' or i == 'T' or i == 'G'):
            return True
        else:
            return False


def info(cs):
    """This function takes the message sent by the user and returns the sequence and a list of the different operations that
    are going to be applied to it"""
    msg = cs.recv(2048).decode('utf-8')
    msg = msg.partition('\n')
    seq = msg[0].upper()
    seq = Seq(seq)
    ops = msg[2].split('\n')

    if msg[0] == '':
        return 'ALIVE'

    elif letters(msg[0]):
        return 'ERROR'
    else:
        return 'OK', seq, ops


def operations(s, cs):
    """This function makes the operations we are requested to do"""

    if info(cs) == 'ALIVE' or info(cs) == 'ERROR':
        return info(cs)

    else:
        result, seq, ops = info(cs)
        methods_name = ['len', 'complement', 'reverse', 'countA', 'countC', 'countT', 'countG', 'percA', 'percC', 'percT',
                        'percG']
        methods = [seq.len(), seq.complement(), seq.reverse(), seq.count('A'), seq.count('C'), seq.count('T'),
                   seq.count('G'), seq.perc('A'), seq.perc('C'), seq.perc('T'), seq.perc('G')]
        count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        out = result + '\n'
        for i in ops:
            for name, op, num in zip(methods_name, methods, count):
                if i == name:
                    out += methods[num] + '\n'
        return out

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen((MAX_CLIENTS))

print('waiting for connections at : {}, {}'.format(IP, PORT))

while True:
    (client_socket, address) = s.accept()

    print("CONNECTION From the IP: {}".format(address))

    msg = operations(s, client_socket)
    print (msg)

    client_socket.close()

