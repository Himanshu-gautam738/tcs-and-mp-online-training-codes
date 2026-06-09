-- Create Source Table
CREATE TABLE SourceData (
    EmpID INT,
    EmpName VARCHAR(50),
    Department VARCHAR(20),
    Quarter VARCHAR(10),
    Revenue INT
);

-- Insert Sample Data
INSERT INTO SourceData VALUES
(1,'John','Sales','Q1',10000),
(2,'Mary','Marketing','Q1',8000),
(3,'Steve','Sales','Q2',12000),
(4,'Anna','Marketing','Q2',9000),
(5,'David','Sales','Q3',15000),
(6,'Sophia','Marketing','Q3',7000);

-- Create Sales Table
CREATE TABLE Sales (
    EmpID INT,
    EmpName VARCHAR(50),
    Department VARCHAR(20),
    Quarter VARCHAR(10),
    Revenue INT
);

-- Create Marketing Table
CREATE TABLE Marketing (
    EmpID INT,
    EmpName VARCHAR(50),
    Department VARCHAR(20),
    Quarter VARCHAR(10),
    Revenue INT
);

-- Insert records into respective tables
INSERT ALL
    WHEN Department = 'Sales' THEN
        INTO Sales (EmpID, EmpName, Department, Quarter, Revenue)
        VALUES (EmpID, EmpName, Department, Quarter, Revenue)
    WHEN Department = 'Marketing' THEN
        INTO Marketing (EmpID, EmpName, Department, Quarter, Revenue)
        VALUES (EmpID, EmpName, Department, Quarter, Revenue)
SELECT * FROM SourceData;

-- View data
SELECT * FROM Sales;
SELECT * FROM Marketing;