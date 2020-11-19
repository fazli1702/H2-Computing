CREATE DATABASE equipment;

CREATE TABLE Device(
    'SerialNumber' INTEGER UNIQUE NOT NULL,
    'Type' CHAR(8) NOT NULL,
    'Model' VARCHAR(50) NOT NULL,
    'Location' VARCHAR(50) NOT NULL,
    'DateOfPurchase' CHAR(10) NOT NULL,
    'Writtenoff' CHAR(5) NOT NULL,
    PRIMARY KEY ('SerialNumber')
);

CREATE TABLE Monitor(
    'SerialNumber' INTEGER REFERENCES Device(SerialNumber),
    'DateCleaned' CHAR(10) NOT NULL
);

CREATE TABLE Laptop(
    'SerialNumber' INTEGER REFERENCES Device(SerialNumber),
    'WeightKg' FLOAT
);

CREATE TABLE Printer(
    'SerialNumber' INTEGER REFERENCES Device(SerialNumber),
    'Toner' VARCHAR(50),
    'DateChanged' CHAR(10)
);