CREATE DATABASE computercompany.db -- create db

CREATE TABLE CUSTOMER (
	CustomerID	VARCHAR(5),
	CustomerName	VARCHAR(50),
	Email	VARCHAR(50),
	Telephone	CHAR(8),
	PRIMARY KEY(CustomerID)
);

CREATE TABLE OFFICE (
	OfficeID	VARCHAR(5),
	PostalCode	CHAR(6),
	Telephone	CHAR(8),
	PRIMARY KEY(OfficeID)
);

CREATE TABLE SALESPERSON (
	SalesPersonID	VARCHAR(5),
	SalesPersonName	VARCHAR(50),
	OfficeID	VARCHAR(5),
	PRIMARY KEY(SalesPersonID),
	FOREIGN KEY(OfficeID) REFERENCES OFFICE(OfficeID)
);

CREATE TABLE SALE (
	SalesPersonID	VARCHAR(5),
	CustomerID	VARCHAR(5),
	SaleDate	CHAR(10),
	Amount	INTEGER,
	PRIMARY KEY(SalesPersonID,CustomerID,SaleDate),
	FOREIGN KEY(SalesPersonID) REFERENCES SALESPERSON(SalesPersonID),
	FOREIGN KEY(CustomerID) REFERENCES CUSTOMER(CustomerID)
);