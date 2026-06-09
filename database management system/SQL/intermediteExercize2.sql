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
(103,'T-Shirt',3,19.99),
(104,'Ergonomic Keyboard',2,49.99);

INSERT INTO sales VALUES
(1,101,2,'2023-01-10'),
(2,102,1,'2023-02-15'),
(3,101,3,'2023-03-05'),
(4,104,12,'2023-03-10');

SELECT *
FROM (
    SELECT 
        p.product_name,
        p.category_id,
        SUM(s.quantity) AS total_quantity,
        DENSE_RANK() OVER(
            PARTITION BY p.category_id
            ORDER BY SUM(s.quantity) DESC
        ) AS rank_position
    FROM products p
    JOIN sales s ON p.product_id = s.product_id
    WHERE YEAR(s.sale_date) = 2023
    GROUP BY p.product_name, p.category_id
) ranked_products
WHERE rank_position <= 3;