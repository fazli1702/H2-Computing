CREATE TABLE Product (
	ProductCode	CHAR(3),
	Name	VARCHAR(50),
	Type	VARCHAR(4),
	Location	VARCHAR(5),
	Price	REAL,
	PRIMARY KEY(ProductCode)
);

CREATE TABLE Cake (
	ProductCode	CHAR(3),
	ServingSize	INTEGER,
	Shape	VARCHAR(5),
	PRIMARY KEY(ProductCode),
	FOREIGN KEY (ProductCode) REFERENCES Product(ProductCode)
);

CREATE TABLE Loaf (
	ProductCode	CHAR(3),
	Weight	INTEGER,
	PRIMARY KEY(ProductCode),
	FOREIGN KEY (ProductCode) REFERENCES Product(ProductCode)
);

CREATE TABLE Bun (
	ProductCode	CHAR(3),
	PiecesPerPackage	INTEGER,
	PRIMARY KEY(ProductCode),
	FOREIGN KEY (ProductCode) REFERENCES Product(ProductCode)
);