import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="a7mdt09040904",
    database="students"
    )

print(mydb)
print("---------------------------")

myCursor=mydb.cursor()

#Delete without inputs:
myCursor.execute("DELETE FROM students WHERE stdFirstName='Taher'")
mydb.commit()

print("Taher Deleted successfully!")

#Take inputs from the user:
sql="DELETE FROM students WHERE stdFirstName=%s"
data=('Nour',)
myCursor.execute(sql, data)
mydb.commit()

print("Nour Deleted successfully!")
