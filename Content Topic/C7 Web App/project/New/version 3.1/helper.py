import sqlite3

def get_classID():
    '''return a list of all the class ID '''
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('SELECT classID FROM class')
    classID = c.fetchall()
    return classID