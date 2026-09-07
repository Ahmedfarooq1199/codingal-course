CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    salary INT,
    age INT
);

INSERT INTO employees VALUES
(1,'Ali','IT',80000,28),
(2,'Ahmed','HR',60000,32),
(3,'Sara','IT',95000,30),
(4,'Ayesha','Finance',75000,27),
(5,'Usman','IT',70000,25);






SELECT * FROM employees;

SELECT name, salary
FROM employees;



SELECT * FROM employees WHERE salary > 70000;

SELECT * FROM employees WHERE salary >= 70000 AND age < 30;

SELECT * FROM employees WHERE department IN ('IT','HR');

SELECT * FROM employees WHERE salary BETWEEN 60000 AND 80000;

SELECT * FROM employees WHERE name LIKE 'A%';



SELECT * FROM employees
ORDER BY salary DESC;



SELECT COUNT(*) FROM employees;

SELECT SUM(salary) FROM employees;

SELECT AVG(salary) FROM employees;

SELECT MAX(salary) FROM employees;

SELECT MIN(salary) FROM employees;



SELECT department, COUNT(*)
FROM employees
GROUP BY department;



SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 70000;