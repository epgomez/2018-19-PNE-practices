import socket

# Create a socket for comunitacting with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')
port = 8081
IP = "212.128.253.102"


#conncet to the server
s.connect((IP, port))

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, port))
    s.send(str.encode(input('message: ')))
    s.close()

msg = s.recv(2048).decode('utf-8')
print(msg)

s.close()

print('the end')