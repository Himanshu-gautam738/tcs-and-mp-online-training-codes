from collections import deque

class BookingQueue:
    def __init__(self):
        self.queue = deque()

    # Add booking to queue
    def enqueue(self, booking):
        self.queue.append(booking)
        print(f"Booking added to queue: {booking}")

    # Remove oldest booking
    def dequeue(self):
        if self.is_empty():
            print("No bookings to process in queue.")
            return None
        return self.queue.popleft()

    # View oldest booking
    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0
