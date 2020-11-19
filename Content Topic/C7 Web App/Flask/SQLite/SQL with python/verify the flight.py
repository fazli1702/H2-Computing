import sqlite3

db = sqlite3.connect('airline.db')
c = db.cursor()

flight_id = input('Enter flight id:')

c.execute('''SELECT origin, destination, duration FROM flights WHERE id = :id''',
          {"id": flight_id})

flight = c.fetchone()


#make sure flight is valif
if flight == None:
    print('Error! No such flight')

else:
    print(flight)
