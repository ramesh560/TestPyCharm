import mysql.connector

myDb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rameshapple",
    database="testbd"
)

mycursor = myDb.cursor()

'''mycursor.execute("CREATE DATABASE testbd")

mycursor.execute("CREATE TABLE students(name VARCHAR (255),age INTEGER(10) )")

mycursor.execute("show tables")

for db in mycursor:
    print(db)'''

mysqlformula = "INSERT INTO students (name, age) values(%s, %s)"
students = [("suresh", 40),
            ("naresh", 35),
            ("sandesh",38),
            ("paresh", 31),
            ("rajesh", 32),
            ("rakesh", 30)]
mycursor.executemany(mysqlformula, students)
myDb.commit()

