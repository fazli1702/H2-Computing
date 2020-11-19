CREATE DATABASE voting_mgm

CREATE TABLE Student (
	MatricNo	CHAR(13) UNIQUE,
	Class	CHAR(2),
	IndexNo	INTEGER,
	Gender	CHAR(1),
	PRIMARY KEY(MatricNo)
);

CREATE TABLE Candidate (
	CandidateNo	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	Name	VARCHAR(50),
	Slogan	VARCHAR(50),
	PotraitLink	VARCHAR(50)
);

CREATE TABLE Vote (
	MatricNo	CHAR(13),
	CandidateNo	INTEGER,
	PRIMARY KEY(MatricNo,CandidateNo),
	FOREIGN KEY(MatricNo) REFERENCES Student(MatricNo),
	FOREIGN KEY(CandidateNo) REFERENCES Candidate(CandidateNo)
);