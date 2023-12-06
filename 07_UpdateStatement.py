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
myCursor.execute("UPDATE students SET stdPassword='a7mdt040904' WHERE stdFirstName='Ahmed'")
mydb.commit()

print("Password Updated successfully!")

#Take inputs from user:

#1
sql="UPDATE students SET stdClass=%s WHERE stdFirstName=%s"
data=('2','Ahmed')
myCursor.execute(sql, data)
mydb.commit()

print("Class Updated successfully!")

#2:
sql="UPDATE students SET stdClass=%s WHERE stdFirstName=%s"
data = [
        ('1', 'Taher'), 
        ('3', 'Nour')
       ]
myCursor.executemany(sql, data)
mydb.commit()

print("Class Updated successfully!")


