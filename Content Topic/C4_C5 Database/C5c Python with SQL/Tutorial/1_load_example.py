# Lesson 4: Using SQLite in Python
# Program 1: load_example.py

import sqlite3
connection = sqlite3.connect("library.db")

connection.close()
