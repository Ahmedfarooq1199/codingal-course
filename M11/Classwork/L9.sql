CREATE TABLE IF NOT EXISTS book (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    rating REAL NOT NULL,
    pages INTEGER NOT NULL,
    pub_year INTEGER NOT NULL
);

INSERT INTO book (book_id, title, genre, rating, pages, pub_year) VALUES
(1, 'The Great Gatsby', 'Fiction', 4.5, 180, 1925),
(2, 'To Kill a Mockingbird', 'Fiction', 4.8, 281, 1960),
(3, '1984', 'Dystopian', 4.7, 328, 1949),
(4, 'Pride and Prejudice', 'Comic', 4.6, 279, 1813),
(5, 'The Catcher in the Rye', 'Fiction', 4.0, 214, 1951);

SELECT * FROM book;

SELECT title, rating FROM book ORDER BY rating ASC;

SELECT title, rating FROM book ORDER BY rating DESC;

SELECT title, rating, genre FROM book ORDER BY genre ASC, rating DESC;

SELECT title, pub_year FROM book ORDER BY pub_year ASC LIMIT 5;

SELECT genre, COUNT(*) AS book_count FROM book GROUP BY genre;

SELECT genre, SUM(pages) AS total_pages ,AVG(rating) AS average_rating FROM book GROUP BY genre;

SELECT genre, COUNT(*) AS book_count FROM book GROUP BY genre HAVING COUNT(*) > 1;

SELECT genre, AVG(rating) AS average_rating
FROM book
GROUP BY genre
HAVING AVG(rating) > 4.5;

