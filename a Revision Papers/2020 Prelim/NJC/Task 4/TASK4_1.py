import sqlite3
import csv

# create db
db = sqlite3.connect('EntryDB.db')
c = db.cursor()


# create table
c.execute('''CREATE TABLE Location (
            LocationID VARCHAR(100),
            Name VARCHAR(100),
            Address VARCHAR(100),
            URL VARCHAR(100),
            PRIMARY KEY (LocationID)
        );''')

c.execute('''CREATE TABLE Visitor (
	NRIC	VARCHAR(20),
	LocationID	VARCHAR(100),
	Name	VARCHAR(100),
	Contact	VARCHAR(20),
	Date	CHAR(10),
	TimeIn	CHAR(5),
	TimeOut	CHAR(5),
	PRIMARY KEY (NRIC, LocationID, Date, TimeIn)
	FOREIGN KEY (LocationID) REFERENCES Location(LocationID)
    );''')


# populate Location table
with open('LOCATIONS.CSV') as f:
    data = csv.reader(f)
    next(data)
    for ele in data:
        c.execute('''INSERT INTO Location VALUES (?,?,?,?)''', ele)


db.commit()
db.close()