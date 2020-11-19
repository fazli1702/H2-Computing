import sqlite3
import csv

db = sqlite3.connect('records.db')
c = db.cursor()


with open('SALES.txt') as f:
    data = csv.reader(f)
    for eid, name, date, sstatus, tsales in data:
        c.execute('INSERT INTO Employee VALUES (?,?,?,?,?)',
                  [name, eid, 'Sales', date, sstatus])
        db.commit()

        c.execute('INSERT INTO Sales VALUES (?,?)', [eid, tsales])
        db.commit()




with open('TECH_SUPPORT.txt') as f:
    data = csv.reader(f)
    for eid, name, date, sstatus, bugsr in data:
        c.execute('INSERT INTO Employee VALUES (?,?,?,?,?)',
                  [name, eid, 'Tech_support', date, sstatus])
        db.commit()

        c.execute('INSERT INTO Tech_support VALUES (?,?)', [eid, bugsr])
        db.commit()




db.close()
