# Lesson 4: Using SQLite in Python
# Program 5: rollback_example.py

import sqlite3

connection = sqlite3.connect("library.db")

connection.execute("INSERT INTO Book(ID, Title) " +
                   "VALUES(1, 'Rollback Book')")
connection.execute("INSERT INTO Book(ID, Title) " +
                   "VALUES(2, 'Also Rollback Book')")
connection.rollback()

connection.execute("INSERT INTO Book(ID, Title) " +
                   "VALUES(3, 'Committed Book')")
connection.commit()

connection.close()
