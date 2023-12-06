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
myCursor.execute("CREATE TABLE subj ( subjCode varchar(25) primary key, subjName varchar(25) not null, subjHours int not null )")

print("Data Base Created successfully!")