import sqlite3

db = sqlite3.connect('pricelist.db')
c = db.cursor()

c.execute('''SELECT * FROM components''')
data = c.fetchall()

print('%-5s %-35s %-8s' % ('id', 'description', 'price'))
print('-' * 50)
for ele in data:
    if ele[0] >= 11:
        break
    
    else:
        print('%-5s %-35s %-8s' % (ele[0], ele[1], ele[2]))        
        

