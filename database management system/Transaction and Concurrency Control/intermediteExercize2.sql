CREATE DATABASE InventoryDB;
USE InventoryDB;

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Stock INT,
    Version INT
);

CREATE TABLE AuditLog (
    LogID INT IDENTITY(1,1) PRIMARY KEY,
    ProductID INT,
    ChangeAmount INT,
    LogTime DATETIME DEFAULT GETDATE()
);

INSERT INTO Products VALUES (1, 100, 1);

-- Procedure
CREATE PROCEDURE UpdateStock
    @ProductID INT,
    @Change INT
AS
BEGIN
    DECLARE @Stock INT, @Version INT, @Retry INT = 0;

    WHILE @Retry < 3
    BEGIN
        SELECT @Stock = Stock, @Version = Version FROM Products WHERE ProductID = @ProductID;

        UPDATE Products
        SET Stock = Stock + @Change, Version = Version + 1
        WHERE ProductID = @ProductID AND Version = @Version;

        IF @@ROWCOUNT > 0
        BEGIN
            INSERT INTO AuditLog (ProductID, ChangeAmount)
            VALUES (@ProductID, @Change);
            RETURN;
        END

        SET @Retry = @Retry + 1;
    END
END;

-- T1 & T2
EXEC UpdateStock 1, -20;
EXEC UpdateStock 1, -30;