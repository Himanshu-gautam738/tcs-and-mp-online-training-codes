CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    state VARCHAR(10)
);

INSERT INTO customers VALUES
(1,'John','Doe','john@example.com','CA'),
(2,'Jane','Smith','jane@example.com','NY'),
(3,'Mike','Lee','mike@example.com','CA');

SELECT state, COUNT(*) AS total_customers
FROM customers
GROUP BY state;