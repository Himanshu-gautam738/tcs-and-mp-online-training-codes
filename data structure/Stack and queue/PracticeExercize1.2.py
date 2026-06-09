from collections import deque

class TaskQueue:
    def __init__(self):
        self.queue = deque()

    # Add a task to the queue
    def enqueue(self, task):
        self.queue.append(task)
        print(f"Task added to queue: {task}")

    # Remove the oldest task
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. No task to remove.")
            return None
        return self.queue.popleft()

    # View the oldest task
    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0
