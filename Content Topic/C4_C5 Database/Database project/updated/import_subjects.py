import sqlite3
import csv


def import_csv_subjects():

    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    f = open("subjects.csv")
    reader = csv.reader(f)



    for ic, subject, level, type in reader:
        db.execute('''INSERT INTO subjects \
            (SubjectID, subject, level, type) \
            VALUES (:SubjectID, :subject, :level, :type)''',
            {"SubjectID":ic, "subject":subject, "level":level, "type":type}) 


    db.commit()
    db.close()
