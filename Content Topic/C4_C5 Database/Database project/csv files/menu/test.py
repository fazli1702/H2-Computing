import sqlite3

db = sqlite3.connect('test.db')
c = db.cursor()

c.execute('''SELECT * FROM test''')

values = c.fetchall()
print(values)
