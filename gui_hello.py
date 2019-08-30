from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def on_click_btn():
    messagebox.showinfo("title is here","Aloha")

root = Tk()

frame = ttk.Frame(root,width=300,height=200)
frame.pack()

btn = ttk.Button(frame, text="Hello",command=on_click_btn)
btn.place(x=100,y=80 )


#event loop ถ้าไม่มี หน้าจอจะปิดทันที
root.mainloop()