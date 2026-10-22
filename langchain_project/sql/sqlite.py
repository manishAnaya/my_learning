import sqlite3

connection = sqlite3.connect('student.db')

cursor = connection.cursor()

table_info = '''
CREATE TABLE STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)
'''

cursor.execute(table_info)

cursor.execute('''INSERT INTO STUDENT VALUES('MANISH', 'GEN AI', 'A', 98)''')
cursor.execute('''INSERT INTO STUDENT VALUES('KRISHNA', 'GEN AI', 'A', 97)''')
cursor.execute('''INSERT INTO STUDENT VALUES('ANAYA', 'GEN AI', 'A', 89)''')
cursor.execute('''INSERT INTO STUDENT VALUES('RAGHAV', 'GEN AI', 'A', 95)''')
cursor.execute('''INSERT INTO STUDENT VALUES('SNEHA', 'GEN AI', 'A', 91)''')
cursor.execute('''INSERT INTO STUDENT VALUES('AARAV', 'GEN AI', 'A', 92)''')

print('the inserted record are: ')

data = cursor.execute('''SELECT * from Student''')

for row in data:
    print(row)