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

sql = "INSERT INTO subj(subjCode, subjName, subjHours) VALUES(%s, %s, %s)"

# if u want to Insert on Value remove the [] and make it execute not executemany
'''
data = ('IS001', 'IS', '3')
myCursor.execut(sql,data)
mydb.commit() 
'''

data = [
        ('IS001', 'IS', '3'), 
        ('Gen002', 'Math3', '3')
       ]

myCursor.executemany(sql,data)
mydb.commit()

print("Data Inserted successfully!")
