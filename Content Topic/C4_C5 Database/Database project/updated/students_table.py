import sqlite3

def add_table_students():

    db = sqlite3.connect('tuition.db')

    try:
        c = db.cursor()
        c.execute('''CREATE TABLE students (\
            nric CHAR ( 9 ) NOT NULL UNIQUE,\
            name VARCHAR ( 50 ) NOT NULL,\
            gender CHAR ( 1 ) NOT NULL,\
            level VARCHAR ( 3 ) NOT NULL,\
            email VARCHAR ( 50 ),
            CHECK(length(nric)=9 AND length(gender)=1),\
            PRIMARY KEY(nric));''')

    except:
        print('Table already exist, cannot create.')


    db.commit()
    db.close()
