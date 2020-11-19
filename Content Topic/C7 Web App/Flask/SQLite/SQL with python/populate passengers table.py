import sqlite3
import csv

db = sqlite3.connect('airline.db')
c = db.cursor()

f = open('passengers.csv')
reader = csv.reader(f)

for name, flight_id in reader:
    print(name, flight_id)
    db.execute('''INSERT INTO passengers (name, flight_id)
                VALUES (:name, :flight_id)''',
               {"name":name, "flight_id":flight_id})

db.commit()
db.close()
