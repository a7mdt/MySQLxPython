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
myCursor.execute("SELECT * FROM subj")
myResult=myCursor.fetchall()

for x in myResult:
    print(x)

print("---------------------------")

myCursor.execute("SELECT subjName FROM subj")
myResult=myCursor.fetchall()

for x in myResult:
    print(x)

print("---------------------------")

myCursor.execute("SELECT subjName, subjCode FROM subj")
myResult=myCursor.fetchall()

for x in myResult:
    print(x)    

print("---------------------------")

myCursor.execute("SELECT * FROM subj")
myResult=myCursor.fetchall()
print(myResult)

print("---------------------------")

myCursor.execute("SELECT * FROM subj")
myResult=myCursor.fetchall()
print(F"{myResult[1]} \n")