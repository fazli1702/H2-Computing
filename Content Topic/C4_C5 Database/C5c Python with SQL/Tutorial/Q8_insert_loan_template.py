# Lesson 4: Using SQLite in Python
# Question 8: insert_loan_template.py

import sqlite3

while True:
    conn = sqlite3.connect("loans.db")

    # Get Borrower ID
    borrower_id = int(input("Enter Borrower ID: "))
    cursor = conn.execute("SELECT COUNT(*) FROM Borrower " +
                          "WHERE ID = ?", (borrower_id,))
    if cursor.fetchone()[0] == 0:
        name = input("Enter Borrower Name: ")
        conn.execute("INSERT INTO Borrower(ID, Name) " +
                     "VALUES(?, ?)", (borrower_id, name))

    # ...fill in the rest of the code below...

    conn.close()
    if input("Quit (Y/N)? ").upper() == "Y":
        break
