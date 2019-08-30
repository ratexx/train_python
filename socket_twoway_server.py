from socket import *

server = socket()

server.bind(("127.0.0.1", 1234))
server.listen(10)

print("Server is ready")

while True:
    socket, address = server.accept()

    print("Connected from", address)

    msg = bytes.decode(socket.recv(1024))

    while msg:
        print(msg)

        socket.send(str.encode(input('> ')))

        msg = bytes.decode(socket.recv(1024))

    socket.close()

    print("Disconnected from", address)
