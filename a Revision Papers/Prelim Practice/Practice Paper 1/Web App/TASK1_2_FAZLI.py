import sqlite3

db = sqlite3.connect('schools.db')
c = db.cursor()

with open('SCHOOL.TXT') as f:
    data = f.readlines()
    school = [ele.strip().split(',') for ele in data]

    for ele in school:
        c.execute('''INSERT INTO School (SchoolCode, Name, Address)
                    VALUES (?, ?, ?)''', ele)
        db.commit()

with open('STAFF.txt') as f:
    data = f.readlines()
    staff = [ele.strip().split(',') for ele in data]
    for ele in staff:
        c.execute('''INSERT INTO Staff (SchoolCode, Name, Department, Contact)
                    VALUES (?, ?, ?, ?)''', ele)
        db.commit()
        

db.close()
