-- Employees table
CREATE TABLE Employees (
    EmployeeID VARCHAR(10) PRIMARY KEY,
    EmployeeName VARCHAR(100),
    Department VARCHAR(50),
    DepartmentHead VARCHAR(100),
    Email VARCHAR(100)
);

INSERT INTO Employees VALUES
('E001','John Smith','Sales','Alice Johnson','john.smith@company.com'),
('E002','Mary Jones','HR','Bob Brown','mary.jones@company.com'),
('E003','Steve Clark','Sales','Alice Johnson','steve.clark@company.com');

SELECT * FROM Employees;