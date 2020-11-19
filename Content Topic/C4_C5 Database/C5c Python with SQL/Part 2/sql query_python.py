import sqlite3

db = sqlite3.connect('airline.db')
c = db.cursor()

##view data

#method 1

c.execute('''SELECT * FROM flights WHERE id = 3;''')

values = c.fetchall()

print(values)



#method 2 (multiple data)

c.execute('''SELECT * FROM flights WHERE destination = 'Paris' OR duration > 500;''')

values = c.fetchall()

for value in value:
    print(value)



#method 3 (single data)

c.execute('''SELECT AVG(duration) FROM flights;''')

values = c.fetchone()   #only one single data

print(values[0])        #since in tupple, return interger/float





##changing data
    
c.execute('''UPDATE flights SET duration = 999
            WHERE origin = 'New York'
            AND destination = 'London';''')


db.commit()
db.close()
