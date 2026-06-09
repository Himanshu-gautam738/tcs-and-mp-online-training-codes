# Base class: Instrument
class Instrument:
    def process_data(self, data):
        """Virtual function to override in derived classes"""
        print(f"Base Instrument processing data: {data}")

    # Function overloading simulation using default args
    def read_data(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            print(f"Reading integer data: {args[0]}")
        elif len(args) == 1 and isinstance(args[0], float):
            print(f"Reading float data: {args[0]}")
        elif len(args) == 0:
            print("Reading data from default sensor source")
        else:
            print("Unsupported read format")


# Derived class: TemperatureSensor
class TemperatureSensor(Instrument):
    def process_data(self, data):
        """Override virtual function"""
        print(f"TemperatureSensor processing temperature data: {data}°C")


# Derived class: PressureSensor
class PressureSensor(Instrument):
    def process_data(self, data):
        """Override virtual function"""
        print(f"PressureSensor processing pressure data: {data} Pa")


# Example usage
if __name__ == "__main__":
    # Compile-time polymorphism simulation
    instr = Instrument()
    instr.read_data()           # No arguments
    instr.read_data(100)        # Integer
    instr.read_data(98.6)       # Float

    print("\n--- Runtime Polymorphism ---")
    instruments = [TemperatureSensor(), PressureSensor()]
    for sensor in instruments:
        sensor.process_data(25)  # Correct overridden method is called
