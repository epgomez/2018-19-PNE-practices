import socket
from Seq import Seq

PORT = 8044
IP = '212.128.253.108'
MAX_CLIENTS = 5

def operations(s, cs):
    """This function makes the operations we are requested to do"""

    msg = cs.recv(2048).decode('utf-8')
    msg = msg.partition('\n')
    seq = msg[0].upper()
    seq = Seq(seq)
    ops = msg[2].split('\n')

    if msg[0] == '':
        result = 'ALIVE'

    elif not (msg[0].upper().strip('ACTG') == ''):
        result = 'ERROR'
    else:
        result = 'OK'

    if result == 'ALIVE' or result == 'ERROR':
        return result
    else:
        methods= {'len':seq.len(), 'complement':seq.complement(), 'reverse':seq.reverse(), 'countA':seq.count('A'),
                        'countC':seq.count('C'), 'countT':seq.count('T'), 'countG':seq.count('G'), 'percA':seq.perc('A'),
                        'percC':seq.perc('C'),'percT':seq.perc('T'),'percG':seq.perc('G')}

        out: str = '{}\nThe sequence is: {}\n'.format(result, seq.strbases)
        for i in ops:
            if i in methods.keys():
                out += str(methods[i]) + '\n'
            else:
                if not (i ==''):
                    out += 'Sorry, that is not a registered operation\n'
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
