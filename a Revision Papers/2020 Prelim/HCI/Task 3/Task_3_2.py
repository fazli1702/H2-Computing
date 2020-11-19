import sqlite3
import csv

db = sqlite3.connect('bakery.db')
c = db.cursor()

with open('CAKES.TXT') as f:
    data = csv.reader(f)
    for code, name, location, price, servesize, shape in data:
        c.execute('''INSERT INTO Product VALUES (?, ?, ?, ?, ?)''',
                  [code, name, 'Cake', location, price])
        db.commit()

        c.execute('INSERT INTO Cake VALUES (?, ?, ?)', [code, servesize, shape])
        db.commit()
        

with open('LOAVES.TXT') as f:
    data = csv.reader(f)
    for code, name, location , price, weight in data:
        c.execute('''INSERT INTO Product VALUES (?, ?, ?, ?, ?)''',
                  [code, name, 'Loaf', location, price])
        db.commit()

        c.execute('INSERT INTO Loaf VALUES (?, ?)', [code, weight])
        db.commit()


with open('BUNS.TXT') as f:
    data = csv.reader(f)
    for code, name, location, price, ppp in data:
        c.execute('''INSERT INTO Product VALUES (?, ?, ?, ?, ?)''',
                  [code, name, 'Bun', location, price])
        db.commit()

        c.execute('INSERT INTO Bun VALUES (?, ?)', [code, ppp])
        db.commit()


db.close()
