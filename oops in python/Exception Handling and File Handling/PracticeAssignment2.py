import csv
import os

# ----------------------------
# Employee Class
# ----------------------------
class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def display(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, "
              f"Position: {self.position}, Salary: {self.salary}")


# ----------------------------
# Employee Management System
# ----------------------------
class EmployeeManager:
    def __init__(self, filename="employees.csv"):
        self.employees = []
        self.filename = filename

    # Add a new employee
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee '{employee.name}' added successfully.")

    # Save all employees to a CSV file
    def save_to_file(self):
        try:
            with open(self.filename, "w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["EmployeeID", "Name", "Position", "Salary"])  # Header
                for emp in self.employees:
                    writer.writerow([emp.emp_id, emp.name, emp.position, emp.salary])
            print(f"All employees saved to '{self.filename}' successfully.")
        except IOError as e:
            print(f"Error writing to file: {e}")

    # Load employees from CSV file
    def load_from_file(self):
        if not os.path.exists(self.filename):
            print(f"File '{self.filename}' not found.")
            return
        try:
            with open(self.filename, "r", newline='', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.employees.clear()  # Clear existing list before loading
                for row in reader:
                    try:
                        emp_id = int(row["EmployeeID"])
                        name = row["Name"]
                        position = row["Position"]
                        salary = float(row["Salary"])
                        employee = Employee(emp_id, name, position, salary)
                        self.employees.append(employee)
                    except (ValueError, KeyError) as e:
                        print(f"Skipping invalid row: {row}. Error: {e}")
            print(f"Employees loaded from '{self.filename}' successfully.")
        except IOError as e:
            print(f"Error reading file: {e}")

    # Display all employees
    def display_employees(self):
        if not self.employees:
            print("No employees available.")
        else:
            print("Employee List:")
            for emp in self.employees:
                emp.display()
