import sqlite3
import csv

db = sqlite3.connect('mypricelist.db')
c = db.cursor()

try:
    c.execute('''CREATE TABLE components (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            price INTEGER);''')

except:
    print('table created')




with open('pricelist.csv') as file:
    reader = csv.reader(file)
    for data in reader:
        description = data[0]
        price = data[1]
        c.execute('''INSERT INTO components (description, price)
                    VALUES (:description, :price)''',
                  {'description':description, 'price':price})

        db.commit()
    
db.close()
