CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    class VARCHAR(20),
    marks INT,
    age INT
);

INSERT INTO students VALUES
(1, 'Ali', '10th', 85, 15),
(2, 'Ahmed', '10th', 72, 16),
(3, 'Sara', '9th', 91, 14),
(4, 'Ayesha', '9th', 78, 15),
(5, 'Usman', '10th', 65, 16),
(6, 'Hina', '9th', 88, 14);

SELECT COUNT(*) AS total_students
FROM students;

SELECT SUM(marks) AS total_marks
FROM students;

SELECT MAX(marks) AS highest_marks
FROM students;

SELECT AVG(marks) AS average_marks
FROM students;

SELECT class, AVG(marks) AS average_marks
FROM students
GROUP BY class
HAVING AVG(marks) > 75;