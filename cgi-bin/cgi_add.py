import cgi
import pymysql

# Insert
form = cgi.FieldStorage()
name = form.getvalue("name")
surname = form.getvalue("surname")
department = form.getvalue("department")
salary = float(form.getvalue("salary"))

#     SQL
connect = pymysql.connect('localhost', 'root', '123', 'mypython', charset='utf8')

try:
    with connect.cursor() as cursor:
        sql = "INSERT INTO employee " \
              "(name, surname, department, salary) " \
              "VALUES(%s, %s, %s, %s)"

        cursor.execute(sql, (name, surname, department, salary))

    connect.commit()
except pymysql.Error:
    connect.rollback()
finally:
    connect.close()

# Redirect
print("Location: cgi_index.py")
print()
