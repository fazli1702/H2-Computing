# Lesson 4: Using SQLite in Python
# Program 8: fetchone_example.py

import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.execute("SELECT ID, Title FROM Book")
row = cursor.fetchone()
while row is not None:
    print(row[1])    # Title is second item in the tuple
    row = cursor.fetchone()
connection.close()
