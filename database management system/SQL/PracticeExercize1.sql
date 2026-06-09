CREATE TABLE employee_hierarchy (
    Entry_Id INT PRIMARY KEY,
    Employee_Name VARCHAR(50),
    Supervisor_Name VARCHAR(50)
);

INSERT INTO employee_hierarchy VALUES
(1,'Jennifer',NULL),
(2,'Andrew','Jennifer'),
(3,'Collin','Andrew'),
(4,'David','Collin'),
(5,'Sophia','Andrew');

SELECT 
Entry_Id,
Employee_Name,
SYS_CONNECT_BY_PATH(Employee_Name,' -> ') AS Reporting_Hierarchy
FROM employee_hierarchy
START WITH Supervisor_Name IS NULL
CONNECT BY PRIOR Employee_Name = Supervisor_Name;