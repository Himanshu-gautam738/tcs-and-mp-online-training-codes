import csv
import os

# ----------------------------
# Book Class
# ----------------------------
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display(self):
        print(f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}")


# ----------------------------
# Library Management Class
# ----------------------------
class Library:
    def __init__(self, filename="books.csv"):
        self.books = []
        self.filename = filename

    # Add a new book
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    # Save all books to a CSV file
    def save_to_file(self):
        try:
            with open(self.filename, "w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["BookID", "Title", "Author"])  # Header
                for book in self.books:
                    writer.writerow([book.book_id, book.title, book.author])
            print(f"All books saved to {self.filename} successfully.")
        except IOError as e:
            print(f"Error writing to file: {e}")

    # Load books from CSV file
    def load_from_file(self):
        if not os.path.exists(self.filename):
            print(f"File '{self.filename}' not found.")
            return
        try:
            with open(self.filename, "r", newline='', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.books.clear()  # Clear existing list before loading
                for row in reader:
                    try:
                        book_id = int(row["BookID"])
                        title = row["Title"]
                        author = row["Author"]
                        book = Book(book_id, title, author)
                        self.books.append(book)
                    except (ValueError, KeyError) as e:
                        print(f"Skipping invalid row: {row}. Error: {e}")
            print(f"Books loaded from {self.filename} successfully.")
        except IOError as e:
            print(f"Error reading file: {e}")

    # Display all books
    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Library Book List:")
            for book in self.books:
                book.display()
