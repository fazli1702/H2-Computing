import sqlite3

db = sqlite3.connect('airline.db')

c = db.cursor()
c.execute('''INSERT INTO flights(origin, destination, duration) \
        VALUES ('New York', 'London', 415) ''')

db.commit()
db.close()
