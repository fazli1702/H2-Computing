import sqlite3
from datetime import date
from calendar import monthrange

'''
This helper.py file consist of helper functions
that executes SQL command in server.py
'''



# ------------------------------ One Student ------------------------------ #

def get_student_password(nric):
    '''return password of user'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('SELECT password FROM student WHERE nric = :nric', {'nric':nric})
    password = c.fetchone()[0]

    return password


def get_student_info(info):
    '''return list of student info'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''SELECT * FROM student WHERE nric = :nric 
                AND password = :password''', info)
    student = c.fetchone()

    return student

def get_student_class_info(nric):
    '''return list of all class info of student'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''SELECT class.subject, class.level, class.teacher, class.location, 
                class.day, class.start_time, class.end_time, class.fee
                FROM class, student, enrollment WHERE 
                student.nric = :nric AND enrollment.nric = student.nric 
                AND enrollment.classID = class.classID''', 
                {'nric':nric})

    student_classes = c.fetchall()

    return student_classes


def get_student_fees(nric):
    '''return total school fee of student'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''SELECT SUM(class.fee) FROM class, enrollment WHERE
                enrollment.nric = :nric AND enrollment.classID = class.classID''',
                {'nric':nric})
    fee = c.fetchone()[0]

    return fee










# ----------------------------- All Students -------------------------------- #

def get_nric():
    '''return list of all student nric'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''SELECT nric FROM student''')
    nric = [ele[0] for ele in c.fetchall()]

    return nric



def get_classID():
    '''return a list of all the class ID '''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('SELECT classID FROM class')
    classID = [ele[0] for ele in c.fetchall()]

    return classID


def get_class_info(classID=None):
    '''return list of all/student class info'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()
    if classID == None:
        c.execute('SELECT * FROM class')
        class_info = c.fetchall()
    
    else:
        c.execute('SELECT * FROM class WHERE classID = :classID', {'classID':classID})
        class_info = c.fetchone()

    return class_info


def get_all_student_info():
    '''return list of all student info'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('SELECT * FROM student')
    students = c.fetchall()

    return students








# --------------------------------- ADD / ENROLL----------------------------------- #




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










# ------------------------------------------------------------------------------------ #

def filter_class_table(subject, location, day):
    filter_info = [subject, location, day]
    '''
    filter selected information 
    to display in display class table

    Case:
    1. 3 None               x1
    2. 3 selected           x1
    3. 2 selected 1 None    x3
    4. 2 None 1 selects     x3
    total: 8 combinations
    '''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()


    # case 1
    if subject == 'None' and location == 'None' and day == 'None':
        return get_class_info()
    
    # case 2
    elif 'None' not in filter_info:
        c.execute('''SELECT * FROM CLASS WHERE subject = :subject AND
                    location = :location AND day = :day''', 
                    {'subject':subject, 'location':location, 'day':day})
        information = c.fetchall()
        return information

    counter = 0
    for ele in filter_info:
        if ele == 'None':
            counter += 1
    
    # case 3
    if counter == 1:
        if subject == 'None':
            c.execute('''SELECT * FROM CLASS WHERE location = :location AND day = :day''', 
                    {'location':location, 'day':day})
            information = c.fetchall()
            return information

        elif location == 'None':
            c.execute('''SELECT * FROM CLASS WHERE subject = :subject AND day = :day''', 
                    {'subject':subject, 'day':day})
            information = c.fetchall()
            return information

        else:
            c.execute('''SELECT * FROM CLASS WHERE subject = :subject AND location = :location''', 
                    {'subject':subject, 'location':location})
            information = c.fetchall()
            return information

    # case 4
    elif counter == 2:
        if subject != 'None':
            c.execute('''SELECT * FROM CLASS WHERE subject = :subject''', 
                    {'subject':subject, 'location':location})
            information = c.fetchall()
            return information

        elif location != 'None':
            c.execute('''SELECT * FROM CLASS WHERE location = :location''', 
                    {'location':location})
            information = c.fetchall()
            return information

        else:
            c.execute('''SELECT * FROM CLASS WHERE day = :day''', 
                    {'day':day})
            information = c.fetchall()
            return information



def check_enrollment(nric, classID):
    '''
    return True if student already 
    enrolled in class
    else return False
    '''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()
    info = [nric, classID]

    c.execute('''SELECT COUNT (nric) FROM enrollment WHERE 
                nric = :nric AND classID = :classID''', info)
    n = c.fetchone()[0]
    print(n)

    if n == 1:
        return True
    else:
        return False



def isEndofMonth() -> bool:
    '''
    check whehter current 
    date is the end of the month
    '''
    today = date.today()
    end = monthrange(today.year, today.month)[1]

    if today.day == end:
        return True
    else:
        return False
