-- Departments table
CREATE TABLE Departments (
    DepartmentID VARCHAR(10) PRIMARY KEY,
    DepartmentName VARCHAR(50),
    DepartmentHead VARCHAR(100)
);

-- Employees table
CREATE TABLE Employees (
    EmployeeID VARCHAR(10) PRIMARY KEY,
    EmployeeName VARCHAR(100),
    DepartmentID VARCHAR(10),
    Email VARCHAR(100)
);

INSERT INTO Departments VALUES
('D01','Sales','Alice Johnson'),
('D02','HR','Bob Brown');

INSERT INTO Employees VALUES
('E001','John Smith','D01','john.smith@company.com'),
('E002','Mary Jones','D02','mary.jones@company.com'),
('E003','Steve Clark','D01','steve.clark@company.com');

SELECT 
Employees.EmployeeID,
Employees.EmployeeName,
Departments.DepartmentName,
Departments.DepartmentHead,
Employees.Email
FROM Employees
INNER JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID;