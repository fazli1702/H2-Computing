import sqlite3

db = sqlite3.connect('school.db')
c = db.cursor()

c.execute('''CREATE TABLE CCAInfo (
	Name VARCHAR(50),
	TeacherIC VARCHAR(50),
	PRIMARY KEY(Name)
);''')

c.execute('''CREATE TABLE Civics(
            Class VARCHAR(50),
            Tutor VARCHAR(50),
            HomeRoom VARCHAR(50),
            PRIMARY KEY(Class)
            );''')

c.execute('''CREATE TABLE Student(
            MatricNo INTEGER,
            Name VARCHAR(50),
            Gender VARCHAR(10),
            CivicsClass VARCHAR(50) REFERENCES Civics(Class),
            PRIMARY KEY(MatricNo)
            );''')

c.execute('''CREATE TABLE StudentCCA(
            MatricNo INTEGER REFERENCES Student(MatricNo),
            CCAName VARCHAR(50) REFERENCES CCAInfo(Name)
            );''')


db.close()
