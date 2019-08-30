import pymysql

connect = pymysql.connect("172.16.0.68","root","123","mypython",charset="utf8",cursorclass=pymysql.cursors.DictCursor)#DicCursor for retrive data field format
try:
    sql = "SELECT * FROM employee LIMIT 100"
    with connect.cursor()as cursor:
        cursor.execute(sql)
        cursor.rowcount
        for row in cursor.fetchall():
            print(row["id"],row["name"])

    print(sql)
except pymysql.Error as err:
    print(err)
finally:
    connect.close()