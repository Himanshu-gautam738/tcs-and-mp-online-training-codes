class Employee:
    def __init__(self, emp_id, name, position, salary, rating):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.rating = rating

    def display(self):
        print(f"{self.emp_id} | {self.name} | {self.position} | {self.salary} | {self.rating}")


class PerformanceReview:
    def __init__(self, emp_id, date, rating, comments):
        self.emp_id = emp_id
        self.date = date
        self.rating = rating
        self.comments = comments

    def display(self):
        print(f"EmpID:{self.emp_id} | Date:{self.date} | Rating:{self.rating} | {self.comments}")


class EmployeeSystem:
    def __init__(self):
        self.employees = []
        self.reviews = []

    def add_employee(self):
        emp_id = int(input("Enter ID: "))
        name = input("Enter name: ")
        position = input("Enter position: ")
        salary = float(input("Enter salary: "))
        rating = float(input("Enter rating: "))
        emp = Employee(emp_id, name, position, salary, rating)
        self.employees.append(emp)
        print("Employee Added\n")

    def display_employees(self):
        if not self.employees:
            print("No employees\n")
            return
        print("\n--- Employees ---")
        for emp in self.employees:
            emp.display()
        print()

    def update_employee(self):
        emp_id = int(input("Enter ID to update: "))
        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.name = input("New name: ")
                emp.position = input("New position: ")
                emp.salary = float(input("New salary: "))
                emp.rating = float(input("New rating: "))
                print("Updated\n")
                return
        print("Employee not found\n")

    def add_review(self):
        emp_id = int(input("Enter employee ID: "))
        found = False
        for emp in self.employees:
            if emp.emp_id == emp_id:
                found = True
        if not found:
            print("Employee not found\n")
            return
        date = input("Enter date: ")
        rating = float(input("Enter rating: "))
        comments = input("Enter comments: ")
        review = PerformanceReview(emp_id, date, rating, comments)
        self.reviews.append(review)
        print("Review added\n")

    def display_reviews(self):
        emp_id = int(input("Enter employee ID: "))
        found = False
        for r in self.reviews:
            if r.emp_id == emp_id:
                r.display()
                found = True
        if not found:
            print("No reviews\n")


system = EmployeeSystem()

while True:
    print("1.Add Employee")
    print("2.Display Employees")
    print("3.Update Employee")
    print("4.Add Review")
    print("5.Display Reviews")
    print("6.Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        system.add_employee()
    elif ch == "2":
        system.display_employees()
    elif ch == "3":
        system.update_employee()
    elif ch == "4":
        system.add_review()
    elif ch == "5":
        system.display_reviews()
    elif ch == "6":
        break
    else:
        print("Invalid choice\n")