import sqlite3
import csv

def import_csv_enrollment():

    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    f = open("enrollment.csv")
    reader = csv.reader(f)

    for sid, cid, g, s, fee  in reader:
        db.execute('''INSERT INTO enrollment \
            (StudentID, ClassID, grade, status, OutstandingFee) \
            VALUES (:StudentID, :ClassID, :grade, :status, :OutstandingFee)''',
            {"StudentID":sid, "ClassID":cid, "grade":g, "status":s, "OutstandingFee":fee}) 


    db.commit()
    db.close()
