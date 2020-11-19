import sqlite3


def add_table_class():

    db = sqlite3.connect('tuition.db')

    try:
        c = db.cursor()
        c.execute('''CREATE TABLE class (\
            `ClassID`	CHAR ( 5 ) NOT NULL UNIQUE,
            `SubjectID`	CHAR ( 3 ) NOT NULL,
            `TeacherID`	CHAR ( 3 ) NOT NULL,
            `CentreID`	VARCHAR ( 2 ) NOT NULL,
            `day`	CHAR ( 3 ) NOT NULL,
            `start`	TIME NOT NULL,
            `end`	TIME NOT NULL,
            CHECK(length(ClassID)=5 AND length(SubjectID)=3
            AND length(TeacherID)=3 AND length(day)=3),
            PRIMARY KEY(`ClassID`),
            FOREIGN KEY(`TeacherID`) REFERENCES `teachers`(`TeacherID`),
            FOREIGN KEY(`SubjectID`) REFERENCES `subjects`(`SubjectID`),
            FOREIGN KEY(`CentreID`) REFERENCES `centres`(`LocationID`));''')

    except:
        print('Table already exist, cannot create.')


    db.commit()
    db.close()
