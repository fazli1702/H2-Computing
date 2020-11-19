import sqlite3

def create_tuition_db():

    db = sqlite3.connect('tuition.db')
    db.close()
