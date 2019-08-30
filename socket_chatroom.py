from tkinter import *
from socket import *
from threading import Thread
from chatroom import ChatRoom


class MyThread(Thread):
    def __init__(self, chat_room_socket):
        super().__init__()

        self.chat_room_socket = chat_room_socket

    def run(self):
        try:
            while True:
                self.chat_room_socket.append_text(
                    bytes.decode(self.chat_room_socket.socket.recv(1024)))
        except (ConnectionAbortedError, ConnectionResetError):
            pass


class ChatRoomSocket(ChatRoom):
    def __init__(self, parent, psocket, pname):
        super().__init__(parent, pname)

        self.socket = psocket

        MyThread(self).start()

    def on_enter_text(self, event):
        sinput = self.str_input

        self.socket.send(str.encode(self.name + ": " + sinput.get()))

        super().on_enter_text(event)


# Main
server = socket()
ip = "172.16.0.68"
port = 1234

try:
    server.bind((ip, port))
    server.listen(10)
    socket, address = server.accept()

    name = "Server"
except OSError:
    socket = server
    socket.connect((ip, port))

    name = "นี่อาจารย์นะ"

root = Tk()
root.title("ChatRoom - " + name)

ChatRoomSocket(root, socket, name)

root.mainloop()

socket.close()
