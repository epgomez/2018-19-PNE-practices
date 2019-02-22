import socket
from Seq import Seq

PORT = 8048
IP = '212.128.253.107'
MAX_CLIENTS = 5


def operations(s, cs):
    """This function makes the operations we are requested to do"""

    msg = cs.recv(2048).decode('utf-8')
    msg = msg.partition('\n')
    seq = msg[0].upper()
    seq = Seq(seq)
    ops = msg[2].split('\n')

    if msg[0] == ' ':
        result = 'ALIVE'

    elif not (msg[0].upper().strip('ACTG') == ''):
        result = 'ERROR'
    else:
        result = 'OK'

    if result == 'ALIVE' or result == 'ERROR':
        return result
    else:
        methods_name = ['len', 'complement', 'reverse', 'countA', 'countC', 'countT', 'countG', 'percA', 'percC',
                        'percT',
                        'percG']
        methods = [seq.len(), seq.complement(), seq.reverse(), seq.count('A'), seq.count('C'), seq.count('T'),
                   seq.count('G'), seq.perc('A'), seq.perc('C'), seq.perc('T'), seq.perc('G')]
        count = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        out: str = '{}\nThe sequence is: {}\n'.format(result, seq.strbases)
        for i in ops:
            for name, op, num in zip(methods_name, methods, count):
                if i == name:
                    out += str(methods[num]) + '\n'
        return out

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(MAX_CLIENTS)

while True:
    print('waiting for connections at : {}, {}'.format(IP, PORT))
    (client_socket, address) = s.accept()

    print("CONNECTION From the IP: {}".format(address))

    msg = operations(s, client_socket)

    info = str.encode(msg)
    client_socket.send(info)
    print('Message sent')
    client_socket.close()
