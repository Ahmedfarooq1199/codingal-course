DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Salesman;

CREATE TABLE Salesman (
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    commission REAL
);

INSERT INTO Salesman (Salesman_id, name, city, commission) VALUES
('S001', 'John Doe', 'New York', 0.10),
('S002', 'Jane Smith', 'Los Angeles', 0.12),
('S003', 'Mike Johnson', 'Chicago', 0.08),
('S004', 'Emily Davis', 'Lahore', 0.15),
('S005', 'David Wilson', 'Phoenix', 0.09);


CREATE TABLE Customer (
    Customer_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    grade TEXT,
    Salesman_id TEXT
);

INSERT INTO Customer (Customer_id, name, city, grade, Salesman_id) VALUES
('C001', 'Alice Brown', 'New York', 'A', 'S001'),
('C002', 'Bob White', 'sialkot', 'B', 'S002'),
('C003', 'Charlie Green', 'Chicago', 'A', 'S003'),
('C004', 'Diana Black', 'Chicago', 'C', 'S004'),
('C005', 'Ethan Blue', 'Phoenix', 'B', 'S005');


CREATE TABLE Orders (
    ord_no TEXT PRIMARY KEY,
    ord_date TEXT,
    Customer_id TEXT,
    Salesman_id TEXT,
    purch_amt REAL
);

INSERT INTO Orders (ord_no, ord_date, Customer_id, Salesman_id, purch_amt) VALUES
('O001', '2023-01-15', 'C001', 'S001', 500),
('O002', '2023-02-20', 'C002', 'S002', 300),
('O003', '2023-03-10', 'C003', 'S003', 700),
('O004', '2023-04-05', 'C004', 'S004', 400),
('O005', '2023-05-12', 'C005', 'S005', 600);


-- 1. Customers and salesmen from the same city

SELECT
    Customer.name AS Customer_Name,
    Salesman.name AS Salesman_Name,
    Salesman.city
FROM Customer
JOIN Salesman
    ON LOWER(Customer.city) = LOWER(Salesman.city);


-- 2. Customers with their salesmen

SELECT
    Customer.name AS Customer_Name,
    Salesman.name AS Salesman_Name
FROM Customer
JOIN Salesman
    ON Customer.Salesman_id = Salesman.Salesman_id;


-- 3. Orders where customer's city does not match salesman's city

SELECT
    Orders.ord_no,
    Customer.name AS Customer_Name,
    Customer.city AS Customer_City,
    Salesman.name AS Salesman_Name,
    Salesman.city AS Salesman_City
FROM Orders
JOIN Customer
    ON Orders.Customer_id = Customer.Customer_id
JOIN Salesman
    ON Orders.Salesman_id = Salesman.Salesman_id
WHERE LOWER(Customer.city) <> LOWER(Salesman.city);