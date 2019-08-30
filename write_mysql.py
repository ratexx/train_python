import pymysql

connect = pymysql.connect("172.16.0.68","root","123","mypython",charset="utf8",cursorclass=pymysql.cursors.DictCursor)#DicCursor for retrive data field format
try:
    sql = "INSERT INTO employee (name,surname,department,salary)"\
          "VALUES(%s,%s,%s,%s)"
    with connect.cursor()as cursor:
        cursor.execute(sql,("ant","ant","ant",4000))
    connect.commit()

    print(sql)
except pymysql.Error as err:
    connect.rollback()
    print(err)
finally:
    connect.close()