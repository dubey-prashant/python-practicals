import sqlite3 as sql 

con = sql.connect('dummy-data/db/students.sqlite')

cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS students')
# cur.commit()

cur.execute('CREATE TABLE students (name TEXT, id INT PRIMARY KEY, age INT );')
# cur.commit()

cur.execute('INSERT INTO students (id, name, age) VALUES (1, "Prashant", 18)')
# cur.commit()

cur.execute('SELECT * FROM students')
for row in cur:
  print(row)
