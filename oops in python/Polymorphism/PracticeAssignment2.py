# Base Class: Appliance
class Appliance:
    def __init__(self, appliance_id, brand):
        self._appliance_id = appliance_id   # Protected attribute
        self._brand = brand

    # Virtual method for calculating power consumption
    def calculate_power(self):
        raise NotImplementedError("Subclasses must implement calculate_power()")

    # Virtual method for displaying appliance details
    def display_details(self):
        print(f"Appliance ID: {self._appliance_id}")
        print(f"Brand: {self._brand}")


# Derived Class: Light
class Light(Appliance):
    def __init__(self, appliance_id, brand, wattage):
        super().__init__(appliance_id, brand)
        self._wattage = wattage

    def calculate_power(self):
        # Assuming usage for 1 hour
        return self._wattage * 1  # Power in Watt-hours

    def display_details(self):
        super().display_details()
        print(f"Type: Light")
        print(f"Wattage: {self._wattage} W")
        print(f"Power Consumption: {self.calculate_power()} Wh")
        print("--------------------------")


# Derived Class: Fan
class Fan(Appliance):
    def __init__(self, appliance_id, brand, speed):
        super().__init__(appliance_id, brand)
        self._speed = speed

    def calculate_power(self):
        # Example formula: Power = Base 50W + 10W per speed level
        return 50 + (10 * self._speed)

    def display_details(self):
        super().display_details()
        print(f"Type: Fan")
        print(f"Speed Level: {self._speed}")
        print(f"Power Consumption: {self.calculate_power()} W")
        print("--------------------------")


# Demonstration of Polymorphism
if __name__ == "__main__":
    # Collection of appliances (base class references)
    appliances = [
        Light(1, "Philips", 60),
        Fan(2, "Orient", 3),
        Light(3, "Havells", 40),
        Fan(4, "Usha", 5)
    ]

    print("=== Appliance Power Consumption ===")
    for appliance in appliances:
        appliance.display_details()
