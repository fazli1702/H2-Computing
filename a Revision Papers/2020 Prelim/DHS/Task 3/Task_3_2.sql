CREATE TABLE Teacher (
	Username	VARCHAR(50),
	Password	VARCHAR(50),
	PRIMARY KEY(Username)
);

CREATE TABLE Student (
	Index	INTEGER,
	Class	CHAR(5),
	PRIMARY KEY(Index)
);

CREATE TABLE Presentation (
	TeacherUsername	VARCHAR(50),
	StudentIndex	INTEGER,
	Date	CHAR(8),
	Marks	INTEGER CHECK(Marks<=100),
	PRIMARY KEY(TeacherUsername,StudentIndex),
	FOREIGN KEY(TeacherUsername) REFERENCES Teacher(Username),
	FOREIGN KEY(StudentIndex) REFERENCES Student(Index)
);