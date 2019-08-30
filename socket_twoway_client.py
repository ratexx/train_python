from socket import *

socket = socket()

socket.connect(("127.0.0.1", 1234))

msg = input('> ')

while msg:
    socket.send(str.encode(msg))

    print(bytes.decode(socket.recv(1024)))

    msg = input('> ')

socket.close()
