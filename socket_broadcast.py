from socket import *
from threading import Thread
from threading import Lock


class BroadcastHandler(Thread):
    lock = Lock()
    handlers = {}   # Static Dictionary

    def __init__(self, psocket, address):
        super().__init__()

        self.socket = psocket
        self.address = address

    def run(self):
        with BroadcastHandler.lock:
            BroadcastHandler.handlers[self.address] = self.socket

        print("Connected from", self.address)

        try:
            while True:
                self.broadcast(bytes.decode(self.socket.recv(1024)))
        except (ConnectionAbortedError, ConnectionResetError):
            pass

        self.socket.close()

        with BroadcastHandler.lock:
            BroadcastHandler.handlers.pop(self.address)

        print("Disconnected from", self.address)

    def broadcast(self, msg):
        with BroadcastHandler.lock:
            for address, psocket in BroadcastHandler.handlers.items():
                if address != self.address:
                    psocket.send(str.encode(msg))


class BroadcastServer:
    def __init__(self, location):
        self.location = location

    def go(self):
        server = socket()

        server.bind(self.location)
        server.listen(10)

        print("Server is ready on port " + str(self.location))

        while True:
            connect, address = server.accept()

            BroadcastHandler(connect, address).start()


# Main
BroadcastServer(("172.16.0.68", 1234)).go()
