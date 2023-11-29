import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('dummy-data/db/example.db')

# Create a cursor object
cur = conn.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# Print all the rows in the table
print("After insertion: ")
for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

# Delete a row of data
cur.execute("DELETE FROM stocks WHERE symbol = 'RHAT'")

# Save (commit) the changes
conn.commit()

# Print all the rows in the table
print("After deletion: ")
for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

# Close the connection
conn.close()
