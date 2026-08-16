CREATE TABLE cashier (
    CashierID INTEGER PRIMARY KEY,
    Name TEXT,
    Username TEXT,
    Password TEXT,
    Phone TEXT,
    Salary REAL
);

INSERT INTO cashier (CashierID, Name, Username, Password, Phone, Salary)
VALUES (1, 'Ali', 'ali123', '12345', '03001234567', 30000);

SELECT * FROM cashier;