import sqlite3

db = sqlite3.connect('airline.db')
c = db.cursor()

c.execute('''SELECT origin, destination, duration FROM flights''')

flights = c.fetchall()

for flight in flights:
    print(flight[0], 'to', flight[1], ',', flight[2], 'minutes.')

db.close()
