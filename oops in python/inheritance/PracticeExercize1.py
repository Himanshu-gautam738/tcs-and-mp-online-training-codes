class Train:
    def __init__(self, tid, name, capacity):
        self.tid = tid
        self.name = name
        self.capacity = capacity

    def update(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def display(self):
        print("ID:", self.tid)
        print("Name:", self.name)
        print("Capacity:", self.capacity)


class PassengerTrain(Train):
    def __init__(self, tid, name, capacity, coaches):
        super().__init__(tid, name, capacity)
        self.coaches = coaches

    def update(self, name, capacity, coaches):
        super().update(name, capacity)
        self.coaches = coaches

    def display(self):
        super().display()
        print("Coaches:", self.coaches)


class FreightTrain(Train):
    def __init__(self, tid, name, capacity, cargo):
        super().__init__(tid, name, capacity)
        self.cargo = cargo

    def update(self, name, capacity, cargo):
        super().update(name, capacity)
        self.cargo = cargo

    def display(self):
        super().display()
        print("Cargo Capacity:", self.cargo)


class RailwaySystem:
    def __init__(self):
        self.trains = []

    def add_train(self):
        tid = int(input("Train ID: "))
        name = input("Train Name: ")
        capacity = int(input("Capacity: "))
        t = Train(tid, name, capacity)
        self.trains.append(t)

    def add_passenger_train(self):
        tid = int(input("Train ID: "))
        name = input("Train Name: "))
        capacity = int(input("Capacity: "))
        coaches = int(input("No of coaches: "))
        t = PassengerTrain(tid, name, capacity, coaches)
        self.trains.append(t)

    def add_freight_train(self):
        tid = int(input("Train ID: "))
        name = input("Train Name: ")
        capacity = int(input("Capacity: "))
        cargo = float(input("Cargo capacity: "))
        t = FreightTrain(tid, name, capacity, cargo)
        self.trains.append(t)

    def display_all(self):
        for t in self.trains:
            print("------")
            t.display()


r = RailwaySystem()

while True:
    print("\n1 Add Train")
    print("2 Add Passenger Train")
    print("3 Add Freight Train")
    print("4 Display All")
    print("5 Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        r.add_train()
    elif ch == "2":
        r.add_passenger_train()
    elif ch == "3":
        r.add_freight_train()
    elif ch == "4":
        r.display_all()
    elif ch == "5":
        break
    else:
        print("Invalid choice")