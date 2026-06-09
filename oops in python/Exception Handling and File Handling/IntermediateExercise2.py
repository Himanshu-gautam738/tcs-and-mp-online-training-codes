# Custom Exception for Empty File
class EmptyFileError(Exception):
    def __init__(self, filename):
        super().__init__(f"Error: File '{filename}' is empty.")


# Function to process a single file
def process_file(filename):
    try:
        with open(filename, "r") as file:
            first_line = file.readline().strip()
            if not first_line:  # File exists but empty
                raise EmptyFileError(filename)
            print(f"First line of '{filename}': {first_line}")
    except FileNotFoundError:
        print(f"{filename} not found")
    except EmptyFileError as e:
        print(e)


# Example usage: list of files
if __name__ == "__main__":
    files_to_process = ["file1.txt", "file2.txt", "file3.txt"]

    for fname in files_to_process:
        process_file(fname)
