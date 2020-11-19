import sqlite3
import csv

db = sqlite3.connect('airline.db')
c = db.cursor()

f = open('flights.csv')
reader = csv.reader(f)
for o, dest, dur in reader:
    db.execute('''INSERT INTO flights (origin, destination, duration)
                VALUES (:origin, :destination, :duration)''',
               {"origin":o, "destination":dest,   "duration":dur})


db.commit()
db.close()
