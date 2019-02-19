import socket
from Seq import Seq

port = 8081
IP = "192.168.0.15"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, port))

msg = 'ADFR'

s.send(msg.encode())