from socket import *

socket = socket()

socket.connect(("172.16.0.167", 4080))

msg = input('> ')

while msg:
    socket.send(str.encode(msg))

    print(bytes.decode(socket.recv(1024)))

    msg = input('> ')

socket.close()
