import socket

port = 8046
IP = "212.128.253.91"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, port))
msg = ''

s.send(msg.encode())

info = s.recv(2048).decode('utf-8')
print(info)

s.close()
