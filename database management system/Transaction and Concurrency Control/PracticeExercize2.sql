CREATE DATABASE AuditDB;
USE AuditDB;

-- Main table
CREATE TABLE Issues (
    RowID INT PRIMARY KEY,
    SecurityID VARCHAR(50),
    Issuer VARCHAR(50),
    IssuerName VARCHAR(100),
    Issue DATE,
    MaturityDate DATE,
    ExpiryDate DATE
);

-- History / Audit table
CREATE TABLE IssueHistory (
    LogID INT IDENTITY(1,1) PRIMARY KEY,
    RowID INT,
    SecurityID VARCHAR(50),
    Issuer VARCHAR(50),
    IssuerName VARCHAR(100),
    Issue DATE,
    MaturityDate DATE,
    ExpiryDate DATE,
    ActionType VARCHAR(10),
    ActionDate DATETIME DEFAULT GETDATE()
);

INSERT INTO Issues VALUES
(1, 'SEC101', 'ABC', 'ABC Ltd', '2020-01-01', '2025-01-01', '2026-01-01');

-- Trigger
CREATE TRIGGER trg_AfterUpdateDelete
ON Issues
AFTER UPDATE, DELETE
AS
BEGIN
    -- Old values (deleted table)
    INSERT INTO IssueHistory
    (RowID, SecurityID, Issuer, IssuerName, Issue, MaturityDate, ExpiryDate, ActionType)
    SELECT RowID, SecurityID, Issuer, IssuerName, Issue, MaturityDate, ExpiryDate, 'OLD'
    FROM DELETED;

    -- New values (inserted table, only for UPDATE)
    INSERT INTO IssueHistory
    (RowID, SecurityID, Issuer, IssuerName, Issue, MaturityDate, ExpiryDate, ActionType)
    SELECT RowID, SecurityID, Issuer, IssuerName, Issue, MaturityDate, ExpiryDate, 'NEW'
    FROM INSERTED;
END;