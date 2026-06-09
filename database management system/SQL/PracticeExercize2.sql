CREATE TABLE securities (
    RowID INT PRIMARY KEY,
    SecurityID VARCHAR(20),
    Issuer VARCHAR(50),
    IssuerName VARCHAR(100),
    IssueDate DATE,
    MaturityDate DATE,
    ExpiryDate DATE
);

CREATE TABLE securities_audit (
    AuditID INT AUTO_INCREMENT PRIMARY KEY,
    RowID INT,
    SecurityID VARCHAR(20),
    Issuer VARCHAR(50),
    IssuerName VARCHAR(100),
    IssueDate DATE,
    MaturityDate DATE,
    ExpiryDate DATE,
    ActionType VARCHAR(20),
    ActionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$

CREATE TRIGGER trg_security_update
AFTER UPDATE ON securities
FOR EACH ROW
BEGIN
    INSERT INTO securities_audit
    (RowID, SecurityID, Issuer, IssuerName, IssueDate, MaturityDate, ExpiryDate, ActionType)
    VALUES
    (OLD.RowID, OLD.SecurityID, OLD.Issuer, OLD.IssuerName, OLD.IssueDate, OLD.MaturityDate, OLD.ExpiryDate, 'UPDATE');
END$$

CREATE TRIGGER trg_security_delete
AFTER DELETE ON securities
FOR EACH ROW
BEGIN
    INSERT INTO securities_audit
    (RowID, SecurityID, Issuer, IssuerName, IssueDate, MaturityDate, ExpiryDate, ActionType)
    VALUES
    (OLD.RowID, OLD.SecurityID, OLD.Issuer, OLD.IssuerName, OLD.IssueDate, OLD.MaturityDate, OLD.ExpiryDate, 'DELETE');
END$$

DELIMITER ;