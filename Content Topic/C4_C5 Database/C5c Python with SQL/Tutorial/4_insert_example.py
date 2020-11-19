# Lesson 4: Using SQLite in Python
# Program 4: insert_example_incomplete.py

import sqlite3

connection = sqlite3.connect("library.db")
connection.execute("INSERT INTO Book (ID, Title) " +
                   "VALUES(0, 'Example Book')")
connection.commit()
connection.close()
