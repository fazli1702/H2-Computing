import sqlite3

db = sqlite3.connect('airline.db')
c = db.cursor()

c.execute('''SELECT origin, destination, duration FROM flights''')

all_data = c.fetchall()
for data in all_data:
    print(data[0], 'to', data[1], ',', data[2], 'minutes.')



db.commit()
db.close()
