CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100),
    Email VARCHAR(100)
);

CREATE TABLE Courses (
    CourseCode VARCHAR(10) PRIMARY KEY,
    Title VARCHAR(100),
    Instructor VARCHAR(100)
);

CREATE TABLE Enrollment (
    StudentID INT,
    CourseCode VARCHAR(10),
    PRIMARY KEY (StudentID, CourseCode),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseCode) REFERENCES Courses(CourseCode)
);

INSERT INTO Students VALUES
(1,'Alice Lee','alice@univ.edu'),
(2,'Bob Smith','bob@univ.edu'),
(3,'Carol Jones','carol@univ.edu');

INSERT INTO Courses VALUES
('CS101','Databases','Dr. Patel'),
('MA101','Calculus','Dr. Gomez'),
('EN150','Literature','Dr. Reed');

INSERT INTO Enrollment VALUES
(1,'CS101'),
(1,'MA101'),
(2,'CS101'),
(3,'EN150');