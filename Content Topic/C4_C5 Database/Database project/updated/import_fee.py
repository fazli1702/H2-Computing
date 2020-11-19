import sqlite3
import csv

def import_csv_fee():

    db = sqlite3.connect('tuition.db')
    c = db.cursor()
    f = open("fees.csv")
    reader = csv.reader(f)

    for t, fee in reader:
        db.execute('''INSERT INTO fee \
                   (type, fee) \
                    VALUES (:type, :fee)''',
                    {"type":t, "fee":fee})


    db.commit()
    db.close()
