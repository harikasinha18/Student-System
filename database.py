import mysql.connector
import sqlite3
mydb = mysql.connector.connect(host="localhost", user="root", passwd="ChinnI@25_", database="student_system")

mycursor = mydb.cursor()
mycursor.execute("select * from Student")


myresult = mycursor.fetchall()

for row in myresult:
    print(row)