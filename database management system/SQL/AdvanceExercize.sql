CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    manager_id INT,
    salary DECIMAL(10,2),
    is_active BOOLEAN,
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);

INSERT INTO employees VALUES
(1,'CEO',NULL,100000,TRUE),
(2,'CTO',1,90000,TRUE),
(3,'Eng Lead',2,80000,TRUE),
(4,'Developer A',3,70000,TRUE),
(5,'Developer B',3,72000,TRUE);

WITH RECURSIVE employee_tree AS (
    SELECT 
        emp_id,
        emp_name,
        manager_id,
        salary,
        1 AS depth
    FROM employees
    WHERE manager_id = 1 AND is_active = TRUE

    UNION ALL

    SELECT 
        e.emp_id,
        e.emp_name,
        e.manager_id,
        e.salary,
        et.depth + 1
    FROM employees e
    JOIN employee_tree et ON e.manager_id = et.emp_id
    WHERE e.is_active = TRUE
)

SELECT 
emp_id,
emp_name,
depth,
salary
FROM employee_tree;