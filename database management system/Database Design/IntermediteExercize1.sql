CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    CustomerPhone VARCHAR(15)
);

CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY,
    ProductCategory VARCHAR(100)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    CategoryID INT,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    SaleDate DATE,
    SaleAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO Customers VALUES
(1,'Alice Smith','9876543210'),
(2,'Bob Lee','9123456789');

INSERT INTO Categories VALUES
(1,'Electronics'),
(2,'Appliances');

INSERT INTO Products VALUES
(1,'Laptop',1),
(2,'Blender',2),
(3,'Mouse',1);

INSERT INTO Sales VALUES
(1,1,1,'2025-06-01',1200),
(2,2,2,'2025-06-02',150),
(3,1,3,'2025-06-03',20);