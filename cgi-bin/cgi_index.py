import pymysql


def stdout_encode(encoding):
    import sys
    import codecs

    sys.stdout = codecs.getwriter(encoding)(sys.stdout.detach())


stdout_encode("utf-8")

print('''Content-type: text/html

<html>
<head>
  <meta charset='utf-8' />
  <title>Employee</title>
</head>
<body>''')

# Data
connect = pymysql.connect('localhost', 'root', '123', 'mypython',
                          charset='utf8',
                          cursorclass=pymysql.cursors.DictCursor)

try:
    with connect.cursor() as cursor:
        sql = "SELECT * FROM employee"

        cursor.execute(sql)

        print("<h3>Employee ({0:d})</h3>".format(cursor.rowcount))

        print("<table border='1' align='center' width='80%'>")

        for row in cursor.fetchall():
            print("<tr>")

            for col in row:
                print("<td>" + str(row[col]) + "</td>")

            print("</tr>")

        print("</table>")
finally:
    connect.close()

# Form
print('''<hr />
<div align='center'>
  <form method='post' action='cgi_add.py'>
    <input type='text' placeholder='name' name='name' />
    <input type='text' placeholder='surname' name='surname' />
    <input type='text' placeholder='department' name='department' />
    <input type='number' placeholder='salary' name='salary' />
    <input type='submit' value='Add' />
  </form>
</div>

</body>
</html>''')
