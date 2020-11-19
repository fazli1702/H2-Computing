import sqlite3

def add_table_subjects():

    db = sqlite3.connect('tuition.db')

    try:
        c = db.cursor()
        c.execute('''CREATE TABLE subjects (\
            SubjectID CHAR ( 3 ) NOT NULL UNIQUE,\
            subject VARCHAR ( 15 ) NOT NULL,\
            level VARCHAR ( 3 ) NOT NULL,\
            type VARCHAR ( 15 ) NOT NULL,\
            CHECK(length(SubjectID)=3),\
            PRIMARY KEY(`SubjectID`));''')

    except:
        print('Table already exist, cannot create.')


    db.commit()
    db.close()
