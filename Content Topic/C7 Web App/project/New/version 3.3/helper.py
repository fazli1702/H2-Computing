import sqlite3

def get_classID():
    '''return a list of all the class ID '''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('SELECT classID FROM class')
    classID = c.fetchall()
    return classID


def get_student_info(info):
    '''return studnet info'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''SELECT * FROM student WHERE nric = :nric 
                AND password = :password''', info)
    student = c.fetchone()
    return student



def add_student(info):
    '''add new student into student table in db'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''INSERT INTO student (nric, name, email, tel, password)
            VALUES (:nric, :name, :email, :tel, :password)''', info)

    print('student info added')
    db.commit()
    db.close()



def enroll_student(info):
    '''enroll student in enrollment table in db'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''INSERT INTO enrollment (nric, classID) VALUES (:nric, :classID)''', info)

    print('student enrolled in enrollment table')
    db.commit()
    db.close()