CREATE DATABASE LogisticsDB;
USE LogisticsDB;

CREATE TABLE Shipments (
    ShipmentID INT PRIMARY KEY,
    Status VARCHAR(50)
);

CREATE TABLE Inventory (
    ProductID INT PRIMARY KEY,
    Quantity INT
);

CREATE TABLE Billing (
    BillID INT IDENTITY(1,1) PRIMARY KEY,
    ShipmentID INT,
    Amount INT
);

INSERT INTO Shipments VALUES (1, 'Pending');
INSERT INTO Inventory VALUES (101, 10);

BEGIN TRANSACTION;

-- Update shipment status
UPDATE Shipments
SET Status = 'Shipped'
WHERE ShipmentID = 1;

-- Savepoint
SAVE TRANSACTION sp1;

-- Inventory update
IF (SELECT Quantity FROM Inventory WHERE ProductID = 101) >= 20
BEGIN
    UPDATE Inventory
    SET Quantity = Quantity - 20
    WHERE ProductID = 101;

    -- Billing
    INSERT INTO Billing (ShipmentID, Amount)
    VALUES (1, 500);

    COMMIT;
END
ELSE
BEGIN
    -- Rollback to savepoint (shipment status remains)
    ROLLBACK TRANSACTION sp1;
    COMMIT;
END;