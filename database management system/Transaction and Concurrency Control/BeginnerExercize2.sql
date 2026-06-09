-- Create Database
CREATE DATABASE ProductDB;
USE ProductDB;

-- Create Table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Price DECIMAL(10,2)
);

-- Insert Sample Data
INSERT INTO Products VALUES (101, 50.00);

-- Connection 1
BEGIN TRANSACTION;

UPDATE Products
SET Price = 60.00
WHERE ProductID = 101;

-- Don't COMMIT yet


-- Connection 2
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

BEGIN TRANSACTION;

SELECT Price
FROM Products
WHERE ProductID = 101;

-- After Connection 1 commits, run again:
SELECT Price
FROM Products
WHERE ProductID = 101;

COMMIT;


-- Back to Connection 1
COMMIT;