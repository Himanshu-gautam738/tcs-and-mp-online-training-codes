# Step 1: Create a Student class
class Student:
    def _init_(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def get_data(self):
        return self.name, self.roll_no, self.grade


# Step 2: Create empty list to store students
students_list = []


# Step 3: Function to add students
def add_students():
    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nEnter details for Student {i + 1}")

        name = input("Enter Name: ")
        roll = input("Enter Roll No: ")
        grade = input("Enter Grade: ")

        student = Student(name, roll, grade)
        students_list.append(student)

    print("\nStudents added successfully!")


# Step 4: Function to display students
def display_students():
    if len(students_list) == 0:
        print("\nNo student data available!")
        return

    print("\n================ Student Records =================")
    print("{:<20} {:<15} {:<10}".format("Name", "Roll No", "Grade"))
    print("-" * 50)

    for student in students_list:
        name, roll, grade = student.get_data()
        print("{:<20} {:<15} {:<10}".format(name, roll, grade))


# Step 5: Main Menu Function
def main_menu():
    while True:
        print("\n========== Student Management Menu ==========")
        print("1. Add Students")
        print("2. Display Students")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_students()
        elif choice == "2":
            display_students()
        elif choice == "3":
            print("\nThank you! Program exited.")
            break
        else:
            print("\nInvalid choice! Please try again.")


# Program start
main_menu()