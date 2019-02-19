import socket
from Seq import Seq

PORT = 8082
IP = '192.168.0.15'
MAX_CLIENTS = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen((MAX_CLIENTS))

(client_socket, address) = s.accept()

print("CONNECTION From the IP: {}".format(address))

msg = client_socket.recv(2048).decode('utf-8')
msg = msg.partition('\n')
seq = msg[0].upper()
seq = Seq(seq)
ops = msg[2].split('\n')

print(msg[0], ops)

