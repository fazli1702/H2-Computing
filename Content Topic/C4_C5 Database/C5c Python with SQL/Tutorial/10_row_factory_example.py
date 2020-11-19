# Lesson 4: Using SQLite in Python
# Program 10: fetchone_example.py

import sqlite3

connection = sqlite3.connect("library.db")
connection.row_factory = sqlite3.Row
cursor = connection.execute("SELECT ID, Title FROM Book")
for row in cursor:
    print(row["Title"])    # row is now a dictionary
connection.close()
