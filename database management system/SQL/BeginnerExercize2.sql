CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price DECIMAL(6,2),
    in_stock BOOLEAN
);

INSERT INTO products VALUES
(101,'Notebook',2.99,TRUE),
(102,'Pen',1.49,TRUE),
(103,'Stapler',15.99,FALSE);

SELECT product_name, price
FROM products
WHERE price < 20
AND in_stock = TRUE;