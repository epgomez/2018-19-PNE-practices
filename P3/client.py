import socket
from Seq import Seq

port = 8081
IP = "212.128.253.112"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, port))

msg = input('Please, enter your sequence and the operations you want to perform, separated by commas: ')
msg = msg.replace(',','\n')
msg = msg.replace(' ','')

s.send(msg.encode())

info = s.recv(2048).decode('utf-8')
print(info)