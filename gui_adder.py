from tkinter import *
from tkinter import ttk
from tkinter.font import nametofont


def on_click_btn(*_):
    try:
        value = float(var_left.get())+float(var_right.get())
        # value = float(entry_left.get())+float(entry_right.get())
        var_result.set(value)
    except ValueError:
        pass


root = Tk()

frame = ttk.Frame(root)
frame.pack()

# First Row
var_left = StringVar()
entry_left = ttk.Entry(frame, width=8, textvariable=var_left)
entry_left.grid(row=0, column=0)
entry_left.bind('<Return>', on_click_btn)

label_add = ttk.Label(frame, text=" + ")
label_add.grid(row=0, column=1)

var_right = StringVar()
entry_right = ttk.Entry(frame, width=8, textvariable=var_right)
entry_right.grid(row=0, column=2)
entry_right.bind('<Return>', on_click_btn)

label_equal = ttk.Label(frame, text=" = ")
label_equal.grid(row=0, column=3)

var_result = StringVar()
label_result = ttk.Label(frame, text="", textvariable=var_result)
label_result.grid(row=0, column=4)

# Second Row
btn_add = ttk.Button(frame, text="Add", command=on_click_btn)
btn_add.grid(row=1, column=2, columnspan=3, sticky="E")

# Font and Padding
nametofont("TkDefaultFont").configure(size=24)
nametofont("TkTextFont").configure(size=24)

for child in frame.winfo_children():
    child.grid_configure(padx=8, pady=8)

# Prepare and Go
entry_left.focus()

root.mainloop()
