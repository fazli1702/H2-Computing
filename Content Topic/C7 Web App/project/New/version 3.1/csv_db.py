import csv
import sqlite3


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

# ----------------------------------------------------------------------------------------- #

'''Create table in db for student, class, enrollment'''

def student_table():
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



# ------------------------------------------------------------------------------------ #



'''add csv file into db for class'''

def add_class():
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



def create_table():
    student_table()
    class_table()
    enrollment_table()

def add_csv():
    add_class()
    # pass

def main():
    drop_table()
    create_table()
    add_csv()

    print()
    print('All task executed succesfully')

main()