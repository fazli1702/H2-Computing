# Lesson 4: Using SQLite in Python
# Program 7: forloop_example.py

import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.execute("SELECT ID, Title FROM Book")
for row in cursor:
    print(row[1])    # Title is second item in the tuple
connection.close()
