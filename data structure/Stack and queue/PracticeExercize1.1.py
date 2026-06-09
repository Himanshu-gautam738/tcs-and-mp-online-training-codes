class TaskStack:
    def __init__(self):
        self.stack = []

    def push(self, task):
        self.stack.append(task)
        print(f"Task added to stack: {task}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. No task to remove.")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
