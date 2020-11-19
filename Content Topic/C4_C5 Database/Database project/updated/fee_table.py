import sqlite3

def add_table_fee():

    db = sqlite3.connect('tuition.db')

    try:
        c = db.cursor()
        c.execute('''CREATE TABLE fee (\
                    type VARCHAR(20) NOT NULL,\
                    fee INT NOT NULL);''')

    except:
        print('Table already exist, cannot create.')


    db.commit()
    db.close()


add_table_fee()
