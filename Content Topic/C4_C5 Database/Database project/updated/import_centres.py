import sqlite3
import csv

def import_csv_centres():

    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    f = open("centres.csv")
    reader = csv.reader(f)



    for ic, location, address, unit, ope, close, tele in reader:
        #print(centre)
        db.execute('''INSERT INTO centres \
            (LocationID, location, address, UnitNo, opening, closing, PhoneNo) \
            VALUES (:LocationID, :location, :address, :UnitNo,:opening, :closing, :PhoneNo)''',
            {"LocationID":ic, "location":location, "address":address, "UnitNo":unit, "opening":ope, "closing":close, "PhoneNo":tele}) 


    db.commit()
    db.close()
