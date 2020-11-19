CREATE TABLE `School` (
	`SchoolCode`	CHAR(4) UNIQUE,
	`Name`	VARCHAR(50),
	`Address`	VARCHAR(50),
	PRIMARY KEY(`SchoolCode`)
);

CREATE TABLE `Staff` (
	`SchoolCode` CHAR(4),
	`Name`	VARCHAR(50),
	`Department`	VARCHAR(50),
	`Contact`	CHAR(8),
	FOREIGN KEY(`SchoolCode`) REFERENCES `School`(`SchoolCode`),
	PRIMARY KEY(`SchoolCode`,`Contact`)
);