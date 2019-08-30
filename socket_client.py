from socket import *
socket = socket()
socket.connect(("172.16.0.167",4080))
socket.recv(1024)#1024 = buffer size
print(bytes.decode(socket.recv(1024)))
socket.close