# Lesson 4: Using SQLite in Python
# Program 9: fetchall_example_print_id.py

import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.execute("SELECT ID, Title FROM Book")
rows = cursor.fetchall()
for row in rows:
    print(row[1])    # Title is second item in the tuple
connection.close()
