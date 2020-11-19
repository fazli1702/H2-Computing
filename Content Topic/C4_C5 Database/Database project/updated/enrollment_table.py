import sqlite3


def add_table_enrollment():


    db = sqlite3.connect('tuition.db')

    try:
        c = db.cursor()
        c.execute('''CREATE TABLE enrollment (\
            `StudentID`	CHAR ( 9 ) NOT NULL,
            `ClassID`	CHAR ( 5 ) NOT NULL,
            `grade`	CHAR ( 1 ),
            `status`	VARCHAR ( 6 ) NOT NULL,
            `OutstandingFee`	INT NOT NULL,
            FOREIGN KEY(`ClassID`) REFERENCES `class`(`ClassID`),
            CHECK(length(StudentID)=9 AND length(ClassID)=5 AND length(grade)=1),
            FOREIGN KEY(`StudentID`) REFERENCES `students`(`nric`),
            PRIMARY KEY(`StudentID`,`ClassID`));''')

    except:
        print('Table already exist, cannot create.')


    db.commit()
    db.close()
