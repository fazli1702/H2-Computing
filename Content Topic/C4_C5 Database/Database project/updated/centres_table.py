import sqlite3

def add_table_centres():

    db = sqlite3.connect('tuition.db')

    try:
        c = db.cursor()
        c.execute('''CREATE TABLE centres (\
            LocationID VARCHAR ( 2 ) NOT NULL UNIQUE,\
            location VARCHAR ( 20 ) NOT NULL,\
            address VARCHAR ( 60 ) NOT NULL,\
            UnitNo VARCHAR ( 10 ) NOT NULL,\
            opening	TIME NOT NULL,\
            closing	TIME NOT NULL,\
            PhoneNo	CHAR ( 8 ) NOT NULL,\
            CHECK(length(PhoneNo)=8),\
            PRIMARY KEY(`LocationID`));''')

    except:
        print('Table already exist, cannot create.')


    db.commit()
    db.close()
