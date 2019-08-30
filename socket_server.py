from socket import *

server = socket()
server.bind(("172.16.0.142", 8888))
server.listen(10) #waiting Queue
print("ready to use")

while True:
    socket, address = server.accept()#input()
    print("connect From > ",address)
    socket.send(str.encode("Server  ส่งเองจ้า")) #byte[]
    socket.close()

