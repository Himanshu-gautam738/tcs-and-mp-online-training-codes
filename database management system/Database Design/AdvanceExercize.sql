CREATE TABLE Accounts (
    AccountID VARCHAR(10),
    Balance DECIMAL(10,2),
    ValidFrom DATE,
    ValidTo DATE,
    PRIMARY KEY (AccountID, ValidFrom)
);

CREATE TABLE Transactions (
    TransID VARCHAR(10) PRIMARY KEY,
    AccountID VARCHAR(10),
    Amount DECIMAL(10,2),
    TransDate DATE
);

INSERT INTO Accounts VALUES
('A1001',5000,'2025-06-01','9999-12-31'),
('A1002',7500,'2025-05-15','9999-12-31');

INSERT INTO Transactions VALUES
('T001','A1001',2000,'2025-06-10'),
('T002','A1001',-500,'2025-06-15'),
('T003','A1002',-1500,'2025-06-18');

DELIMITER $$

CREATE TRIGGER account_versioning
AFTER INSERT ON Transactions
FOR EACH ROW
BEGIN
    UPDATE Accounts
    SET ValidTo = NEW.TransDate
    WHERE AccountID = NEW.AccountID
    AND ValidTo = '9999-12-31';

    INSERT INTO Accounts(AccountID,Balance,ValidFrom,ValidTo)
    SELECT 
        AccountID,
        Balance + NEW.Amount,
        NEW.TransDate,
        '9999-12-31'
    FROM Accounts
    WHERE AccountID = NEW.AccountID
    ORDER BY ValidFrom DESC
    LIMIT 1;
END$$

DELIMITER ;

SELECT *
FROM Accounts
WHERE AccountID = 'A1001'
AND '2025-06-12' BETWEEN ValidFrom AND ValidTo;

CREATE INDEX idx_account_time
ON Accounts(AccountID, ValidFrom, ValidTo);