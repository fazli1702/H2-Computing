import sqlite3

def add_table_teachers():


    db = sqlite3.connect('tuition.db')

    try:
        c = db.cursor()
        c.execute('''CREATE TABLE teachers (\
            TeacherID CHAR ( 3 ) NOT NULL UNIQUE,\
            name VARCHAR ( 50 ) NOT NULL,\
            PhoneNo CHAR ( 8 ) NOT NULL,\
            email VARCHAR ( 30 ) NOT NULL,\
            CHECK(length(TeacherID)=3 AND length(PhoneNo)=8),\
            PRIMARY KEY(TeacherID));''')

    except:
        print('Table already exist, cannot create.')


    db.commit()
    db.close()
