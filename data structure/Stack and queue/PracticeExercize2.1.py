class BookingStack:
    def __init__(self):
        self.stack = []

    def push(self, booking):
        self.stack.append(booking)
        print(f"Booking added to stack: {booking}")

    def pop(self):
        if self.is_empty():
            print("No bookings to remove from stack.")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
