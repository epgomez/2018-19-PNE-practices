import socket
from Seq import Seq

PORT = 8041
IP = '212.128.253.109'
MAX_CLIENTS = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen((MAX_CLIENTS))

(client_socket, address) = s.accept()

def letters(ms):
    ms = ms.upper()
    if ms.strip('ACTG')=='':
        return False
    else:
        return True

def info(cs):
    """This function takes the message sent by the user and returns the sequence and a list of the different operations that
    are going to be applied to it"""
    msg = cs.recv(2048).decode('utf-8')
    msg = msg.partition('\n')
    seq = msg[0].upper()
    seq = Seq(seq)
    ops = msg[2].split('\n')
    print('recevi')
    if msg[0] == '':
        return 'ALIVE', '', ''

    elif letters(msg[0]):
        return 'ERROR', '', ''
    else:
        return 'OK', seq, ops

print('h')
print(info(client_socket))