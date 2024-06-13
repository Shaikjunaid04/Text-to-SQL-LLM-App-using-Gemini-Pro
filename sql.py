import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
Create table STUDENT (NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)


cursor.execute('''Insert Into STUDENT values('Alex','Data Science', 'A',98)''')
cursor.execute('''Insert Into STUDENT values('John','Data Science', 'A',96)''')
cursor.execute('''Insert Into STUDENT values('Alexandra','Computer Science', 'B',90)''')
cursor.execute('''Insert Into STUDENT values('James','Cyber Security', 'B',88)''')
cursor.execute('''Insert Into STUDENT values('Warner','Applied Math', 'C',79)''')
cursor.execute('''Insert Into STUDENT values('Richie','Computer Science', 'A',95)''')
cursor.execute('''Insert Into STUDENT values('William','Cyber Security', 'B',89)''')
cursor.execute('''Insert Into STUDENT values('Amanda','Applied Math', 'B',85)''')

print("The inserted records are")

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)


connection.commit()
connection.close