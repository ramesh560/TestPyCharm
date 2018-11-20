import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rameshapple",
    database="testbd"
)

myCursor = mydb.cursor()

myCursor.execute("SELECT name FROM students")
myData = myCursor.fetchall()
for row in myData:
    print(row)
mydb.close()