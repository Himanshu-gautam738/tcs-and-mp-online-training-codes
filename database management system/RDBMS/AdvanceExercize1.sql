-- Create Sales table
CREATE TABLE Sales (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    SalesAmount INT
);

-- Insert Sample Data
INSERT INTO Sales VALUES
(1,'Alpha',12000),
(2,'Beta',7000),
(3,'Gamma',3000),
(4,'Delta',4000);

-- CASE + Aggregation Query
SELECT 
CASE
    WHEN SalesAmount >= 10000 THEN 'High Sales'
    WHEN SalesAmount >= 5000 AND SalesAmount < 10000 THEN 'Medium Sales'
    ELSE 'Low Sales'
END AS SalesCategory,
COUNT(*) AS NumberOfProducts
FROM Sales
GROUP BY
CASE
    WHEN SalesAmount >= 10000 THEN 'High Sales'
    WHEN SalesAmount >= 5000 AND SalesAmount < 10000 THEN 'Medium Sales'
    ELSE 'Low Sales'
END;