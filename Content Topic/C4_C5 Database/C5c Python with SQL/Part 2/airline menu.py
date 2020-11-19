def menu():
    while True:
        print()
        print('***** Flights Information System *****')
        print()
        print(' 1. List all the flights')
        print(' 2. Check a flight')
        print(' 3. Display passengers list')
        print()
        print(' X. Quit')
        print()


        choice = input('Enter your choice: ')

        if choice.upper() == 'X':
            return None         #or break
        
        elif int(choice) == 1:
            list_all_flights()
            
        elif choice == '2':
            check_flight()
            
        elif choice == '3':
            display_passengers_list()
            
        else:
            print('Please enter a valid choice.')



import sqlite3


def list_all_flights():
    db = sqlite3.connect('airline.db')
    c = db.cursor()

    c.execute('''SELECT origin, destination, duration FROM flights''')

    flights = c.fetchall()

    for flight in flights:
        print(flight[0], 'to', flight[1], ',', flight[2], 'minutes.')

    db.commit()
    db.close()

#list_all_flights()

def check_flight():
    flight_id = input("\nChoose a Flight ID: ")
              
    db = sqlite3.connect('airline.db')
    c = db.cursor()          
    c.execute('''SELECT origin, destination, duration FROM flights
                WHERE id = :id''',
                {"id": flight_id})

    flight = c.fetchone()
              
    if flight == None:
        print('Error: No such flights.')
    else:
        print(flight)

    #check_flight()
              
def display_passengers_list():
    flight_id = input("\nChoose a Flight ID: ")
              
    db = sqlite3.connect('airline.db')
    c = db.cursor()          
    c.execute('''SELECT origin, destination, duration FROM flights
                WHERE id = :id''',
                {"id": flight_id})

    flight = c.fetchone()
              
    if flight == None:
        print('Error: No such flights.')
    else:
        #List passengers
        c.execute('''SELECT name FROM passengers \
                    WHERE "flight_id" = :flight_id''', \
                    {"flight_id": flight_id})

        passengers = c.fetchall()

        if len(passengers) == 0:
            print('No passenger.')
            
        else:
            print("\nPassengers:")
            for passenger in passengers:
                print("\t", passenger[0])

        

#display_passengers_list()




menu()
