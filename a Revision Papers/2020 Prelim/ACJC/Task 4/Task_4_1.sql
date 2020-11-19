CREATE TABLE Employee (
	Employee_name	VARCHAR(50),
	Employee_ID	INTEGER,
	Job_type	VARCHAR(15),
	Date_of_employement	CHAR(10),
	Service_status	VARCHR(5),
	PRIMARY KEY(Employee_ID)
);

CREATE TABLE Sales (
	Employee_ID	INTEGER,
	Sales	INTEGER,
	PRIMARY KEY(Employee_ID)
);

CREATE TABLE Tech_support (
	Employee_ID	INTEGER,
	Bugs_resolved	INTEGER,
	PRIMARY KEY(Employee_ID)
);