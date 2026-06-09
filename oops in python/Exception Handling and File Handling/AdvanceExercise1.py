import time
import random  # For simulation purposes

# Function to simulate writing to a file (can fail randomly for demonstration)
def write_to_file(filename, message):
    # Simulate random I/O failure (for demonstration)
    if random.choice([True, False]):
        raise IOError("Simulated I/O error")
    
    with open(filename, "a") as f:
        f.write(message + "\n")
    print(f"Written to {filename}: {message}")


# Reliable logging function
def log_message(message, primary="app.log", fallback="backup.log", retries=3):
    attempt = 0
    while attempt < retries:
        try:
            write_to_file(primary, message)
            return  # Success
        except IOError as e:
            attempt += 1
            print(f"Attempt {attempt}: Failed to write to {primary}. Error: {e}")
            time.sleep(0.5)  # Wait before retrying

    # All retries failed, write to fallback
    try:
        write_to_file(fallback, message)
        print(f"All retries failed. Logged to fallback: {fallback}")
    except IOError as e:
        print(f"Critical failure: Could not write to fallback file. Error: {e}")


# Example usage
if __name__ == "__main__":
    messages = [
        "System started successfully.",
        "User logged in.",
        "Error connecting to database."
    ]

    for msg in messages:
        log_message(msg)
