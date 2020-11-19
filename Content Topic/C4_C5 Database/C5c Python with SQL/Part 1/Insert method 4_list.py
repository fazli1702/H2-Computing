import sqlite3

datalist = [('New York', 'Paris', 435),('Moscow', 'Paris', 245), ('Lima', 'New York', 455)]


db = sqlite3.connect('airline.db')
c = db.cursor()

for data in datalist:
    c.execute('''INSERT INTO flights(origin, destination, duration) \
                VALUES(:origin, :destination, :duration)''', data)

db.commit()
db.close()

