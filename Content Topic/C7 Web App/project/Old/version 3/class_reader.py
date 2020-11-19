import sqlite3

def display_student_class(nric):
    '''display all of student information using nric number'''
    nric = nric.upper()
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''SELECT class.subject, class.level, class.teacher, class.location, 
                class.day, class.start_time, class.end_time, class.fee
                FROM class, student, enrollment WHERE 
                student.nric = :nric AND enrollment.nric = student.nric 
                AND enrollment.classID = class.classID''', 
                {'nric':nric})

    student_class = c.fetchone()

    return student_class



def get_classID():
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('SELECT classID FROM class')
    lst = c.fetchall()
    return lst
