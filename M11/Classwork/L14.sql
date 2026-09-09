DROP TABLE IF EXISTS Sales;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;


CREATE TABLE Customers (
    Customer_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT
);

INSERT INTO Customers (Customer_id, name, city) VALUES
('C001', 'Ali Khan', 'Lahore'),
('C002', 'Ahmed Raza', 'Karachi'),
('C003', 'Sara Malik', 'Islamabad'),
('C004', 'Hassan Ali', 'Lahore'),
('C005', 'Ayesha Noor', 'Multan');



CREATE TABLE Products (
    Product_id TEXT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL
);

INSERT INTO Products (Product_id, product_name, category, price) VALUES
('P001', 'Laptop', 'Electronics', 85000),
('P002', 'Mobile Phone', 'Electronics', 45000),
('P003', 'Keyboard', 'Accessories', 3500),
('P004', 'Mouse', 'Accessories', 2000),
('P005', 'Printer', 'Electronics', 25000);



CREATE TABLE Sales (
    Sale_id TEXT PRIMARY KEY,
    Customer_id TEXT,
    Product_id TEXT,
    quantity INTEGER,
    sale_date TEXT
);

INSERT INTO Sales (Sale_id, Customer_id, Product_id, quantity, sale_date) VALUES
('S001', 'C001', 'P001', 1, '2026-01-10'),
('S002', 'C002', 'P002', 2, '2026-01-12'),
('S003', 'C003', 'P003', 3, '2026-02-05'),
('S004', 'C004', 'P004', 5, '2026-02-15'),
('S005', 'C005', 'P005', 1, '2026-03-01');



SELECT * FROM Sales;



SELECT
    Sales.Sale_id,
    Customers.name AS Customer_Name,
    Products.product_name,
    Sales.quantity,
    Products.price
FROM Sales
JOIN Customers
    ON Sales.Customer_id = Customers.Customer_id
JOIN Products
    ON Sales.Product_id = Products.Product_id;


SELECT
    Sales.Sale_id,
    Customers.name AS Customer_Name,
    Products.product_name,
    Sales.quantity,
    Products.price,
    Sales.quantity * Products.price AS Total_Amount
FROM Sales
JOIN Customers
    ON Sales.Customer_id = Customers.Customer_id
JOIN Products
    ON Sales.Product_id = Products.Product_id;



SELECT
    Sales.Sale_id,
    Products.product_name,
    Sales.quantity * Products.price AS Total_Amount
FROM Sales
JOIN Products
    ON Sales.Product_id = Products.Product_id
WHERE Sales.quantity * Products.price > 50000;



SELECT
    Products.product_name,
    SUM(Sales.quantity) AS Total_Quantity,
    SUM(Sales.quantity * Products.price) AS Total_Sales
FROM Sales
JOIN Products
    ON Sales.Product_id = Products.Product_id
GROUP BY Products.product_name;



SELECT
    Customers.name AS Customer_Name,
    SUM(Sales.quantity * Products.price) AS Total_Sales
FROM Sales
JOIN Customers
    ON Sales.Customer_id = Customers.Customer_id
JOIN Products
    ON Sales.Product_id = Products.Product_id
GROUP BY Customers.name;


SELECT
    AVG(Sales.quantity * Products.price) AS Average_Sale
FROM Sales
JOIN Products
    ON Sales.Product_id = Products.Product_id;