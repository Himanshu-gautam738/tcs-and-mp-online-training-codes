CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY,
    AuthorName VARCHAR(100)
);

CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(200),
    PublicationYear INT
);

CREATE TABLE BookAuthors (
    BookID INT,
    AuthorID INT,
    PRIMARY KEY (BookID, AuthorID),
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

INSERT INTO Authors VALUES
(1,'Jane Austen'),
(2,'Mark Twain');

INSERT INTO Books VALUES
(1,'Pride and Prejudice',1813),
(2,'Adventures of Tom Sawyer',1876),
(3,'Emma',1815);

INSERT INTO BookAuthors VALUES
(1,1),
(2,2),
(3,1);