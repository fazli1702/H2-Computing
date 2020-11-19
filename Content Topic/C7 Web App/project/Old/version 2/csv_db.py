import sqlite3
import csv


def drop_table():
    '''drop all table'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    try:
        c.execute('''DROP TABLE student''')
        c.execute('''DROP TABLE class''')
        c.execute('''DROP TABLE enrollment''')
        print('All tables are dropped')
    except:
        print('Tables already dropped')

    db.commit()
    db.close()
    


def student_table():
    '''create student table and add data from csv to db'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    # create table
    try:
        c.execute('''CREATE TABLE student(
            nric VARCHAR(9) PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            tel INTERGER,
            password VARCHAR(32) NOT NULL);''')
        print('table student successfully created')

    except:
        print('table already exist')

    db.commit()
    db.close()


def class_table():
    '''create class table and add data from csv to db'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    # create table
    try:
        c.execute('''CREATE TABLE class(
            classID VARCHAR(3) PRIMARY KEY,
            subject VARCHAR(20) NOT NULL,
            level VARCHAR(2) NOT NULL,
            teacher VARCAHR(50) NOT NULL,
            location VARCHAR(50) NOT NULL,
            day VARCHAR(10) NOT NULL,
            start_time TIME NOT NULL,
            end_time TIME NOT NULL,
            fee INT NOT NULL
        );''')
        print('table class successfully created')

    except:
        print('table already exist')
		


    db.commit()
    db.close()


def enrollment_table():
    '''create enrollment table and add data from csv to db'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    # create table
    try:
        c.execute('''CREATE TABLE enrollment(
            nric NOT NULL,
            classID NOT NULL,
            PRIMARY KEY (nric, classID),
            FOREIGN KEY (nric) REFERENCES student (nric),
            FOREIGN KEY (classID) REFERENCES class (classID)
        );''')
        print('table enrollment successfully created')

    except:
        print('table already exist')

    db.commit()
    db.close()


	
def add_class():
    '''add data into class table'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    with open('class.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            c.execute('''INSERT INTO class 
            (classID,subject,level,teacher,location,day,start_time,end_time,fee)\
            VALUES (:classID,:subject,:level,:teacher,:location,:day,:start_time,:end_time,:fee)''',
            row)
        print('class.csv added into database')

        db.commit()
        db.close()	


def add_student():
    '''add data into student table'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    with open('student.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            c.execute('''INSERT INTO student (nric, name, email, tel, password)
            VALUES (:nric, :name, :email, :tel, :password)''', row)
        print('student.csv added into database')

        db.commit()
        db.close()



def add_enrollment():
    '''add data into enrollment table'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    with open('enrollment.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            c.execute('''INSERT INTO enrollment (nric, classID) VALUES (:nric, :classID)''', row)
        print('enrollment.csv added into database')

        db.commit()
        db.close()
	
	
	

def create_table():
    student_table()
    enrollment_table()
    class_table()

def add_table():
    add_class()
    # add_student()
    # add_enrollment()
    

def main():
    drop_table()
    create_table()
    add_table()
    print()
    print('all task executed successfully')

