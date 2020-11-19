import sqlite3
db = sqlite3.connect('airline.db')
c = db.cursor()

datalist = [('Istanbul', 'Tokyo', 700),
            ('New York', 'Paris', 435),
            ('Moscow', 'Paris', 245),
            ('Lima', 'New York', 455)]

for data in datalist:
    c.execute('''INSERT INTO flights(origin, destination, duration)
                VALUES(:origin, :destination, :duration)''', data)

db.commit()
db.close()
