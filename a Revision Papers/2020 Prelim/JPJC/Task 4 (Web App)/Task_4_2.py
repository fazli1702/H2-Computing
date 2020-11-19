import sqlite3
import csv

db = sqlite3.connect('computercompany.db')
c = db.cursor()


with open('CUSTOMER.CSV') as f:
    data = csv.reader(f)
    next(f)
    for ele in data:
        c.execute('INSERT INTO CUSTOMER VALUES(?, ?, ?, ?)', ele)
    


with open('OFFICE.CSV') as f:
    data = csv.reader(f)
    next(f)
    for ele in data:
        c.execute('INSERT INTO OFFICE VALUES (?, ?, ?)', ele)



with open('SALESPERSON.CSV') as f:
    data = csv.reader(f)
    next(f)
    for ele in data:
        c.execute('INSERT INTO SALESPERSON VALUES (?, ?, ?)', ele)



with open('SALE.CSV') as f:
    data = csv.reader(f)
    next(f)
    for ele in data:
        c.execute('INSERT INTO SALE VALUES (?, ?, ?, ?)', ele)



db.commit()
db.close()
