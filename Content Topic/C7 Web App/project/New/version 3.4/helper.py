import sqlite3

# ------------- One Student -------------- #

def get_password(nric):
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

# ------------ All Students -------------- #

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


def get_class_info():
    '''return list of all class info'''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('SELECT * FROM class')
    class_info = c.fetchall()

    return class_info





# --------------------------------------------------------- #




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



# ------------------------------------------------------------------- #

def filter_class_table(subject, location, day):
    filter_info = [subject, location, day]
    '''
    filter selected information 
    to display in display class table

    Case:
    1. 3 None
    2. 3 selected
    3. 2 selected 1 None
    4. 2 None 1 selects
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

    # case 

    