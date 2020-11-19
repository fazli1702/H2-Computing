import sqlite3
import csv

def import_csv_class():

    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    f = open("class.csv")
    reader = csv.reader(f)



    for cid, sid, tid, ceid, d, s, e in reader:
        db.execute('''INSERT INTO class \
            (ClassID, SubjectID, TeacherID, CentreID, day, start, end) \
            VALUES (:ClassID, :SubjectID, :TeacherID, :CentreID, :day, :start, :end)''',
            {"ClassID":cid, "SubjectID":sid, "TeacherID":tid, "CentreID":ceid, "day":d, "start":s, "end":e})
        


    db.commit()
    db.close()
