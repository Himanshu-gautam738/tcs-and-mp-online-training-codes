CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(100),
    Author VARCHAR(100),
    Year INT,
    Genre VARCHAR(50)
);

INSERT INTO Books (BookID, Title, Author, Year, Genre)
VALUES
(1, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Novel'),
(2, 'To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
(3, '1984', 'George Orwell', 1949, 'Dystopian');

SELECT * FROM Books;