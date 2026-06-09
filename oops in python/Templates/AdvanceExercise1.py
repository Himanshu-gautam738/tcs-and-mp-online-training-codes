# === Policy Classes ===

class ConsoleLogger:
    def log(self, message: str) -> None:
        print(f"[Console] {message}")

class NullLogger:
    def log(self, message: str) -> None:
        pass  # Do nothing

class FileLogger:
    def log(self, message: str) -> None:
        print(f"[File] {message} (written to file)")

# === Component Class ===
class Component:
    def __init__(self, policy):
        self.policy = policy  # Injected behavior

    def perform_task(self) -> None:
        self.policy.log("Task started.")
        # Component-specific logic here
        self.policy.log("Task completed.")

# === Usage Example ===
if __name__ == "__main__":
    # Component with console logging
    console_component = Component(ConsoleLogger())
    console_component.perform_task()

    # Component with no logging
    silent_component = Component(NullLogger())
    silent_component.perform_task()

    # Component with file logging
    file_component = Component(FileLogger())
    file_component.perform_task()
