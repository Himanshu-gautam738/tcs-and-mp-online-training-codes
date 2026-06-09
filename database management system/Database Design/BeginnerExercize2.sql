CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100),
    Email VARCHAR(100)
);

CREATE TABLE Course (
    CourseCode VARCHAR(10) PRIMARY KEY,
    Title VARCHAR(100),
    Instructor VARCHAR(100)
);

CREATE TABLE Enrollment (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseCode VARCHAR(10),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseCode) REFERENCES Course(CourseCode)
);

INSERT INTO Student VALUES
(1,'Alice Lee','alice@univ.edu'),
(2,'Bob Smith','bob@univ.edu'),
(3,'Carol Jones','carol@univ.edu');

INSERT INTO Course VALUES
('CS101','Databases','Dr. Patel'),
('MA201','Calculus','Dr. Gomez'),
('EN150','Literature','Dr. Reed');

INSERT INTO Enrollment VALUES
(1,1,'CS101'),
(2,1,'MA201'),
(3,2,'CS101'),
(4,3,'EN150');