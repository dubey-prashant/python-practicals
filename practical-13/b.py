#	Write a python program to import CSV file in SQLite database.

import csv
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('dummy-data/db/example.db')

# Create a cursor object
cur = conn.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS MyTable
             (Name text, Age text, Class text)''')

# Open the CSV file
with open('dummy-data/data.csv', 'r') as f:
    # Create a CSV reader
    reader = csv.reader(f)
    
    # Skip the header row
    next(reader)
    
    # Insert rows from the CSV file into the table
    for row in reader:
        cur.execute("INSERT INTO MyTable VALUES (?, ?, ?)", row)

# Save (commit) the changes
conn.commit()

# Print all the rows in the table
print("After reading CSV: ")
for row in cur.execute('SELECT * FROM MyTable'):
    print(row)

# Close the connection
conn.close()
