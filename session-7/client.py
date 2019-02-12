# creating a client for the teacher server

import socket

# Create a sopcket for comunitacting with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')

port = 8080
IP = "212.128.253.64"


#conncet to the server
s.connect((IP, port))

s.send(str.encode('hehehe'))

msg = s.recv(2048).decode('utf-8')
print(msg)

s.close()

print('the end')