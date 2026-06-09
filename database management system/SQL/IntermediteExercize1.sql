CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(50)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category_id INT,
    price DECIMAL(10,2),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    quantity INT,
    sale_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO categories VALUES
(1,'Books'),
(2,'Electronics'),
(3,'Clothing');

INSERT INTO products VALUES
(101,'SQL Guide',1,29.99),
(102,'Headphones',2,89.99),
(103,'T-Shirt',3,19.99);

INSERT INTO sales VALUES
(1,101,2,'2023-01-10'),
(2,102,1,'2023-02-15'),
(3,101,3,'2023-03-05');

SELECT 
c.category_name,
COALESCE(SUM(s.quantity * p.price),0) AS total_revenue
FROM categories c
LEFT JOIN products p ON c.category_id = p.category_id
LEFT JOIN sales s ON p.product_id = s.product_id
AND s.sale_date BETWEEN '2023-01-01' AND '2023-03-31'
GROUP BY c.category_name;