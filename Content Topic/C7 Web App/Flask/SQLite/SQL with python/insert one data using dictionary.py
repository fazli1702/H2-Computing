import sqlite3
db = sqlite3.connect('airline.db')
c = db.cursor()

c.execute('''INSERT INTO flights (origin, destination, duration)
             VALUES(:origin, :destination, :duration)''',
           {'origin':'Shanghai', 'destination':'Paris', 'duration':760})


db.commit()
db.close()
