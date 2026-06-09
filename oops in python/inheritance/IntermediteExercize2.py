class Human:
    def __init__(self, name):
        self.name = name


class Employee(Human):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id


class RemoteWorker:
    def __init__(self, location):
        self.location = location


class RemoteEmployee(Employee, RemoteWorker):
    def __init__(self, name, employee_id, location):
        Employee.__init__(self, name, employee_id)
        RemoteWorker.__init__(self, location)

    def show_details(self):
        print("Name:", self.name)
        print("ID:", self.employee_id)
        print("Location:", self.location)


emp = RemoteEmployee("Rahul", 101, "Work From Home")
emp.show_details()