import sqlite3
import csv

db = sqlite3.connect('tuition centre')
c = db.cursor()

f = open("student info.csv")
reader = csv.reader(f)

for ic, name, gender, level in reader:
    db.execute('''INSERT INTO student \
        (NRIC, Name, Gender, Level) \
        VALUES(:NRIC, :Name, :Gender, :Level)''',
        {"NRIC":ic, "Name":name, "Gender":gender, "Level":level})

db.commit()
db.close()
