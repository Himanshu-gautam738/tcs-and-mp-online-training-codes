from collections import deque

class MinQueue:
    def __init__(self):
        self.queue = deque()
        self.min_queue = deque()

    def enqueue(self, x):
        self.queue.append(x)

        while self.min_queue and self.min_queue[-1] > x:
            self.min_queue.pop()

        self.min_queue.append(x)

    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
            return

        removed = self.queue.popleft()

        if removed == self.min_queue[0]:
            self.min_queue.popleft()

    def get_min(self):
        if not self.min_queue:
            print("Queue is empty")
            return None
        return self.min_queue[0]

# Driver code
mq = MinQueue()

mq.enqueue(5)
mq.enqueue(3)
mq.enqueue(7)
mq.enqueue(2)

print("Minimum:", mq.get_min())

mq.dequeue()
print("Minimum after dequeue:", mq.get_min())

mq.dequeue()
print("Minimum after dequeue:", mq.get_min())
