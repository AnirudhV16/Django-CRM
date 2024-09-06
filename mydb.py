import mysql.connector

DataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
)

CursorObject= DataBase.cursor()
CursorObject.execute("CREATE DATABASE customers")

print("all done")