from tkinter import *
from tkinter import ttk
import pymysql


class Employee(ttk.Frame):
    def __init__(self, parent, pconnect):
        super().__init__(parent)

        self.connect = pconnect
        self.tv_main = ttk.Treeview(self)

        self.create_ui()
        self.load_data()
        self.pack(fill=BOTH, expand=True)

    def create_ui(self):
        tv = self.tv_main

        tv['columns'] = ('name', 'surname', 'department', 'salary')

        tv.heading('#0', text='ID')
        tv.column('#0', width=64)

        tv.heading('name', text='Name')
        tv.column('name', anchor='w', width=256)
        tv.heading('surname', text='Surname')
        tv.column('surname', anchor='w', width=256)
        tv.heading('department', text='Department')
        tv.column('department', anchor='w', width=256)
        tv.heading('salary', text='Salary')
        tv.column('salary', anchor='e', width=128)

        # <Double-1>, <Button-1>, <<TreeviewSelect>>
        tv.bind("<Double-1>", self.on_dbclick_btn)  # no "index out of range"

        tv.pack(fill=BOTH, expand=True)

    def load_data(self):
        with connect.cursor() as cursor:
            sql = "SELECT * FROM employee"

            cursor.execute(sql)

            for row in cursor.fetchall():
                self.tv_main.insert(
                    '', 'end', text=row["id"],
                    values=(row["name"], row["surname"], row["department"],
                            "{0:,d}".format(row["salary"])))

    def on_dbclick_btn(self, _):
        tv = self.tv_main

        if tv.selection():
            item = tv.selection()[0]
            emp_id = tv.item(item, "text")

            tv.delete(item)

            with connect.cursor() as cursor:
                sql = "DELETE FROM employee " \
                      "WHERE id=%s"

                cursor.execute(sql, (emp_id, ))

            connect.commit()


# Main
connect = pymysql.connect('172.16.0.68', 'root', '123', 'mypython',
                          charset='utf8',
                          cursorclass=pymysql.cursors.DictCursor)

try:
    root = Tk()
    root.title("Employee")

    Employee(root, connect)

    root.mainloop()
finally:
    connect.close()
