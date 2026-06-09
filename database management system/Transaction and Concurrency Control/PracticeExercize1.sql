CREATE DATABASE SecurityDB;
USE SecurityDB;

-- Main table
CREATE TABLE Securities (
    RowID INT PRIMARY KEY,
    SecurityID VARCHAR(50),
    Issuer VARCHAR(50),
    IssuerName VARCHAR(100),
    Issue DATE,
    MaturityDate DATE,
    ExpiryDate DATE,
    DeletedFlag BIT DEFAULT 0
);

-- Log table
CREATE TABLE DeleteLog (
    LogID INT IDENTITY(1,1) PRIMARY KEY,
    RowID INT,
    DeletedBy VARCHAR(100),
    DeletedAt DATETIME DEFAULT GETDATE()
);

INSERT INTO Securities VALUES
(1, 'SEC101', 'ABC', 'ABC Ltd', '2020-01-01', '2025-01-01', '2026-01-01', 0);

-- Trigger
CREATE TRIGGER trg_BeforeDelete
ON Securities
INSTEAD OF DELETE
AS
BEGIN
    -- Log who and which row
    INSERT INTO DeleteLog (RowID, DeletedBy)
    SELECT RowID, SYSTEM_USER FROM DELETED;

    -- Soft delete
    UPDATE Securities
    SET DeletedFlag = 1
    WHERE RowID IN (SELECT RowID FROM DELETED);
END;