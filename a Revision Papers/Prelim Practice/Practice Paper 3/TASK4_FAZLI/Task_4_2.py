import csv
import sqlite3


def students():
    db = sqlite3.connect('result_mgm.db')
    c = db.cursor()
    with open('students.csv') as f:
        data = csv.reader(f)
        next(data)

        for ele in data:
            c.execute('''INSERT INTO Student (MatricNo, Name, Class, IndexNo, Gender)
                        VALUES (?, ?, ?, ?, ?)''', ele)
            db.commit()
        print('Student information added')
    db.close()


def test():
    db = sqlite3.connect('result_mgm.db')
    c = db.cursor()
    
    with open('tests.csv') as f:
        data = csv.reader(f)
        next(data)
        for ele in data:
            c.execute('''INSERT INTO Test (TestID, Subject, Level, MaxScore, Year, Term, Percentage)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''', ele)
            db.commit()
        print('Test information added')
    db.close()
        

def results():
    db = sqlite3.connect('result_mgm.db')
    c = db.cursor()
    
    with open('results.csv') as f:
        data = csv.reader(f)
        next(data)
        for ele in data:
            c.execute('''INSERT INTO Result (MatricNo, TestID, Score) VALUES (?, ?, ?)''', ele)
            db.commit()
        print('Result information added')

    db.close()

def main():
    students()
    test()
    results()
    

##main()

    
