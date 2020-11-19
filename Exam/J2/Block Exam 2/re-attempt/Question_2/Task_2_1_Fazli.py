import csv
import sqlite3



def create_table():
    # create table
    db = sqlite3.connect('school.db')
    c = db.cursor()

    # CCAInfo
    c.execute('''
    CREATE TABLE CCAInfo(
        Name VARCHAR(50) PRIMARY KEY,
        TeacherIC VARCHAR(50)
    );
        ''')


    # civics
    c.execute('''
    CREATE TABLE Civics(
        Class VARCHAR(20) PRIMARY KEY,
        Tutor VARCHAR(50),
        HomeRoom VARCHAR(20)
    );
    ''')


    # Student
    c.execute('''
    CREATE TABLE Student(
        MatricNo INTEGER PRIMARY KEY,
        Name VARCHAR(50),
        Gender CHAR(1),
        CivicsClass VARCHAR(10) REFERENCES Civics(MatriNo)
    );
    ''')


    # Student CCA
    c.execute('''
    CREATE TABLE StudentCCA(
        MatricNo INTEGER REFERENCES Student(MatricNo),
        CCAName VARCHAR(50) REFERENCES CCAInfo(Name)
    );
    ''')

    db.commit()
    db.close()



# read file & add into db
db = sqlite3.connect('school.db')
c = db.cursor()

with open('CCAInfo.csv') as f:
    data = csv.reader(f)
    next(data)
    for ele in data:
        c.execute('''INSERT INTO CCAInfo (Name, TeacherIC) VALUES (:name, :ic)''', ele)
        db.commit()



with open('Civics.csv') as f:
    data = csv.reader(f)
    next(data)
    for ele in data:
        c.execute('''INSERT INTO Civics (Class, Tutor, HomeRoom)
                    VALUES (:Class, :Tutor, :HomeRoom)''', ele)
        db.commit()



with open('Student.csv') as f:
    data = csv.reader(f)
    next(data)
    for ele in data:
        c.execute('''INSERT INTO Student (MatricNo, Name, Gender, CivicsClass)
                    VALUES (:MatricNo, :Name, :Gender, :CivicsClass)''', ele)
        db.commit()



with open('StudentCCA.csv') as f:
    data = csv.reader(f)
    next(data)
    for ele in data:
        c.execute('''INSERT INTO StudentCCA (MatricNo, CCAName)
                    VALUES (:MatricNo, :CCAName)''', ele)
        db.commit()

db.close()