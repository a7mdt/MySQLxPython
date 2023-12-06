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

sql="SELECT * FROM students WHERE stdFirstName=%s"
data=("Menna",)
myCursor.execute(sql, data)
myResult=myCursor.fetchall()
print(myResult)

print("---------------------------")

myCursor.execute("SELECT * FROM students ORDER BY stdFirstName")
myResult=myCursor.fetchall()

print("==>Its The Default of Ordring :")
for x in myResult:
    print(x)

print("---------------------------")

myCursor.execute("SELECT * FROM students ORDER BY stdFirstName ASC")
myResult=myCursor.fetchall()

print("==>Its The ASC of Ordring :")
for x in myResult:
    print(x)

print("---------------------------")

myCursor.execute("SELECT * FROM students ORDER BY stdFirstName DESC")
myResult=myCursor.fetchall()

print("==>Its The DESC of Ordring :")
for x in myResult:
    print(x)

print("---------------------------")

myCursor.execute("SELECT * FROM students LIMIT 4")
myResult=myCursor.fetchall()

print("==>Its The Limit of Ordring :")
for x in myResult:
    print(x)    

print("---------------------------")

myCursor.execute("SELECT * FROM students LIMIT 5 OFFSET 2")
myResult=myCursor.fetchall()

print("==>Its The Offset of Ordring :")
for x in myResult:
    print(x)    