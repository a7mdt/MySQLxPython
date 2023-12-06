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

#ADD a NEW COLUMN :
myCursor.execute("ALTER TABLE students ADD COLUMN stdClass varchar(20)")
mydb.commit()

print("Column added successfully!")

#UPDATE an OLD COLUMN :
myCursor.execute("ALTER TABLE students CHANGE srdPassword stdPassword varchar(25)")
mydb.commit()

print("Column Updated successfully!")