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
    #list passengers
    c.execute('''SELECT name FROM passengers WHERE flight_id = :flight_id''',
              {"flight_id": flight_id})

    passengers = c.fetchall()

    if len(passengers) == 0:
        print("No passenger.")
        
    else:
        print("\nPassengers:")
        for passenger in passengers:
            print(passenger[0])
