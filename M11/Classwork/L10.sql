CREATE TABLE activities (
    id INT PRIMARY KEY,
    activity_name VARCHAR(100),
    activity_type VARCHAR(50),
    duration INT,
    calories INT
);

INSERT INTO activities VALUES
(1, 'Running', 'Cardio', 30, 300),
(2, 'Cycling', 'Cardio', 45, 400),
(3, 'Push Ups', 'Strength', 20, 150),
(4, 'Weight Lifting', 'Strength', 40, 250),
(5, 'Walking', 'Cardio', 60, 200),
(6, 'Squats', 'Strength', 30, 220);

SELECT * 
FROM activities
ORDER BY duration DESC;

SELECT activity_type, COUNT(*) AS activity_count
FROM activities
GROUP BY activity_type;

SELECT 
    AVG(duration) AS average_duration,
    AVG(calories) AS average_calories
FROM activities;