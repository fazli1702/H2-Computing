import sqlite3
import csv

db = sqlite3.connect('airline.db')
c = db.cursor()

f = open("passengers.csv")
reader = csv.reader(f)


##try:
##    c = db.cursor()
##    c.execute('''CREATE TABLE passengers (\
##            id INTEGER PRIMARY KEY AUTOINCREMENT,\
##            name VARCHAR(10) NOT NULL,\
##            flight_id INTEGER NOT NULL \
##            REFERENCES flights(id));''')
##
##except:
##    print('Table already exist, cannot create.')

for name, flight in reader:
    db.execute('''INSERT INTO passengers \
        (name, flight_id) \
        VALUES (:name, :flight_id)''',
        {"name":name, "flight_id":flight})


db.commit()
db.close()
