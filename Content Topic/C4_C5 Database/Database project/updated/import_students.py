import sqlite3
import csv

def import_csv_students():

    db = sqlite3.connect('tuition.db')
    c = db.cursor()
    f = open("students.csv")
    reader = csv.reader(f)

    for ic, name, gender, level, email in reader:
        db.execute('''INSERT INTO students \
                   (nric, name, gender, level, email) \
                    VALUES (:nric, :name, :gender, :level, :email)''',
                    {"nric":ic, "name":name, "gender":gender, "level":level, "email":email})


    db.commit()
    db.close()
