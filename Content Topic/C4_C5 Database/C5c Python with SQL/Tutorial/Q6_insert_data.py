# Lesson 4: Using SQLite in Python
# Question 6: insert_example_incomplete.py

import sqlite3

connection = sqlite3.connect("library.db")
while True:
    try:
        book_id = int(input("Enter Book ID: "))
    except ValueError:
        print("Not a valid ID")
        continue
    title = input("Enter Title: ")
    try:
        
        connection.commit()
    except sqlite3.DatabaseError:
        print("Database error (e.g., duplicate ID)")
        continue
    print("Insertion successful!")
    if input("Quit (Y/N)? ").upper() == "Y":
        break
connection.close()
