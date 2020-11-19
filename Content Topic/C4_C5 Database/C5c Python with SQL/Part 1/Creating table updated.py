import sqlite3

db = sqlite3.connect('airline.db')

try:
    c = db.cursor()
    c.execute('''CREATE TABLE flights (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        origin VARCHAR(20) NOT NULL,\
        destination VARCHAR(20) NOT NULL,\
        duration INTEGER NOT NULL);''')

except:
    print('Table already exist, cannot create.')


db.commit()
db.close()
        
