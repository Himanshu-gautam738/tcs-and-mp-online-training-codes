-- Create Database
CREATE DATABASE BankDB;
USE BankDB;

-- Create Table
CREATE TABLE Accounts (
    AccountID INT PRIMARY KEY,
    Balance INT
);

-- Insert Sample Data
INSERT INTO Accounts VALUES (1, 500);
INSERT INTO Accounts VALUES (2, 300);

-- Transaction
BEGIN TRANSACTION;

IF (SELECT Balance FROM Accounts WHERE AccountID = 1) >= 100
BEGIN
    UPDATE Accounts
    SET Balance = Balance - 100
    WHERE AccountID = 1;

    UPDATE Accounts
    SET Balance = Balance + 100
    WHERE AccountID = 2;

    COMMIT;
END
ELSE
BEGIN
    ROLLBACK;
END;