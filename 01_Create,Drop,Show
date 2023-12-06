import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="a7mdt09040904",
    # database="students"
    )

print(mydb)
print("---------------------------")

myCursor=mydb.cursor()

myCursor.execute("CREATE DATABASE itsDB_fromVScode")
myCursor.execute("DROP DATABASE itsDB_fromVScode") # We will see an Error if there isn't a DB with this Name.
myCursor.execute("DROP DATABASE IF EXISTS itsDB_fromVScode") # The code will run But Without an Error.

myCursor.execute("SHOW DATABASES")
for db in myCursor:
    print(db)