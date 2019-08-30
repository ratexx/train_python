from tkinter import *
from tkinter import ttk


class ChatRoom(ttk.Frame):
    def __init__(self, parent, name="A"):
        super().__init__(parent)

        self.name = name
        self.text_output = Text(self, state=DISABLED)
        self.str_input = StringVar()
        self.text_input = ttk.Entry(self, textvariable=self.str_input)

        self.create_ui()
        self.pack(fill=BOTH, expand=True)

    def create_ui(self):
        # Output
        toutput = self.text_output

        toutput.pack(fill=BOTH, expand=True)

        # Input
        tinput = self.text_input

        tinput.bind("<Return>", self.on_enter_text)
        tinput.focus()
        tinput.pack(fill=X)

    def on_enter_text(self, event):
        sinput = self.str_input

        self.append_text(self.name + ": " + sinput.get())

        sinput.set("")

    def append_text(self, text):
        toutput = self.text_output

        toutput.config(state=NORMAL)
        toutput.insert(END, text + "\n")
        toutput.see(END)
        toutput.config(state=DISABLED)


# Main
if __name__ == '__main__':
    root = Tk()
    root.title("ChatRoom")

    ChatRoom(root)

    root.mainloop()
