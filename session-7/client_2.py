import socket

# Create a sopcket for comunitacting with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')
port = 8081
IP = "212.128.253.82"


#conncet to the server
s.connect((IP, port))

while True:
    s.send(str.encode(input('message: ')))

msg = s.recv(2048).decode('utf-8')
print(msg)

s.close()

print('the end')