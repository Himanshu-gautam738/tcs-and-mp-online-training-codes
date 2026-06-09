file_name = "numbers.txt"  # The file should contain two numbers, one per line

try:
    # Attempt to open and read the file
    with open(file_name, "r") as file:
        lines = file.readlines()
        
        if len(lines) < 2:
            raise ValueError("File does not contain enough numbers.")
        
        # Convert the first two lines to numbers
        num1 = float(lines[0].strip())
        num2 = float(lines[1].strip())
        
        # Attempt division
        result = num1 / num2
        print(f"Result of dividing {num1} by {num2} is {result}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except ValueError as ve:
    print(f"Error: {ve}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
