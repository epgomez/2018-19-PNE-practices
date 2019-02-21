import socket

port = 8046
IP = "212.128.253.109"

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, port))
    msg = input('Please, enter your sequence and the operations you want to perform, separated by commas: ')
    if msg != '':
        msg = msg.replace(',','\n')
        msg = msg.replace(' ','')

    else:
        msg = ' '

    s.send(msg.encode())

    info = s.recv(2048).decode('utf-8')
    print(info)

    s.close()