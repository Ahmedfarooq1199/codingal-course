CREATE TABLE student (
    Name TEXT,
    Rollno INTEGER,
    Class TEXT,
    Section TEXT
);

INSERT INTO student (Name, Rollno, Class, Section) VALUES
('John Doe', 1, '10th Grade', 'A'),
('Jane Smith', 2, '10th Grade', 'B'),
('Alice Johnson', 3, '11th Grade', 'A'),
('Bob Brown', 4, '11th Grade', 'B');

SELECT * FROM student;


CREATE TABLE IF NOT EXISTS Salesman (
    Salesman_id TEXT,
    Name TEXT,
    City TEXT,
    Commission REAL
);

INSERT INTO Salesman (Salesman_id, Name, City, Commission) VALUES
('S001', 'John Doe', 'New York', 0.10),
('S002', 'Jane Smith', 'Los Angeles', 0.12),
('S003', 'Alice Johnson', 'Chicago', 0.15),
('S004', 'Bob Brown', 'Houston', 0.08);

SELECT * FROM Salesman;


SELECT Name, City
FROM Salesman
WHERE City = 'New York';
