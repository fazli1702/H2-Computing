import sqlite3
import csv

def import_csv_teachers():

    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    f = open("teachers.csv")
    reader = csv.reader(f)

    for ic, name, no, email in reader:
        db.execute('''INSERT INTO teachers \
            (TeacherID, name, PhoneNo, email) \
            VALUES (:TeacherID, :name, :PhoneNo, :email)''',
            {"TeacherID":ic, "name":name, "PhoneNo":no, "email":email}) 


    db.commit()
    db.close()
