# Lesson 4: Using SQLite in Python
# Program 2: create_example.py

import sqlite3
connection = sqlite3.connect("library.db")
connection.execute("CREATE TABLE Book " +
                   "(ID INTEGER PRIMARY KEY, Title TEXT)")
connection.commit()
connection.close()
