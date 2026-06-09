# File name
file_name = "example.txt"

# Predefined message
message = "Welcome to file handling!"

# 1. Write message to file
with open(file_name, "w") as file:
    file.write(message)
    print(f"Message written to {file_name}")

# 2. Read content from file and display
with open(file_name, "r") as file:
    content = file.read()
    print("Content of the file:")
    print(content)
