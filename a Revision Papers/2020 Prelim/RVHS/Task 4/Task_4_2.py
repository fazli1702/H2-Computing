import csv
import sqlite3

db = sqlite3.connect('voting_mgm.db')
c = db.cursor()

with open('students.csv') as f:
    data = csv.reader(f)
    next(data)
    for matricNo, Class, index, gender in data:
        c.execute('''INSERT INTO Student VALUES (?, ?, ?, ?)''',
                  [matricNo, Class, index, gender])
        db.commit()

with open('candidates.csv') as f:
    data = csv.reader(f)
    next(data)
    for CandidateNo, Name, Slogan, PortraitLink in data:
        c.execute('''INSERT INTO Candidate VALUES (?, ?, ?, ?)''',
                  [CandidateNo, Name, Slogan, PortraitLink])
        db.commit()


with open('votes.csv') as f:
    data = csv.reader(f)
    next(data)
    for MatricNo, CandidateNo in data:
        c.execute('''INSERT INTO Vote VALUES (?, ?)''',
                  [MatricNo, CandidateNo])
        db.commit()



db.close()
        
