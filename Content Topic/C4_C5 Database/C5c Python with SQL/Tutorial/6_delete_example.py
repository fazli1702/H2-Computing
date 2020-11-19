# Lesson 4: Using SQLite in Python
# Program 6: delete_example.py

import sqlite3

connection = sqlite3.connect("library.db")

# Insert some rows first so we have something to delete
connection.execute("INSERT INTO Book(ID, Title) " +
                   "VALUES(4, 'Extra Book')")
connection.execute("INSERT INTO Book(ID, Title) " +
                   "VALUES(5, 'Also Extra Book')")
connection.commit()

# Ask for ID and delete the corresponding row
book_id = input("Enter Book ID to delete: ")
connection.execute("DELETE FROM Book WHERE ID = ?", (book_id,))
connection.commit()

connection.close()
