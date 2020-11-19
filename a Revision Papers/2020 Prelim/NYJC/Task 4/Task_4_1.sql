CREATE TABLE Registration (
	StudentID	CHAR(10),
	Type	CHAR(1),
	Venue	VARCHAR(50),
	Session	CHAR(2),
	PRIMARY KEY(StudentID)
);

CREATE TABLE Arts (
	StudentID	CHAR(6),
	Performace	VARCHAR(5),
	FOREIGN KEY(StudentID) REFERENCES Registration(StudentID),
	PRIMARY KEY(StudentID)
);

CREATE TABLE Cultural (
	StudentID	CHAR(6),
	Race	VARCHAR(20),
	FOREIGN KEY(StudentID) REFERENCES Registration(StudentID),
	PRIMARY KEY(StudentID)
);

CREATE TABLE Sports (
	StudentID	CHAR(6),
	Contact	VARCHAR(2),
	Cost	INTEGER,
	FOREIGN KEY(StudentID) REFERENCES Registration(StudentID),
	PRIMARY KEY(StudentID)
);