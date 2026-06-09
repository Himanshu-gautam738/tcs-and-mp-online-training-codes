# Create objects
booking_stack = BookingStack()
booking_queue = BookingQueue()

# Stack operations (Recent bookings)
booking_stack.push("Ticket#101")
booking_stack.push("Ticket#102")
booking_stack.push("Ticket#103")

print("Most recent booking:", booking_stack.peek())
print("Cancelled booking:", booking_stack.pop())
print("Is booking stack empty?", booking_stack.is_empty())

print()

# Queue operations (Booking requests)
booking_queue.enqueue("Ticket#201")
booking_queue.enqueue("Ticket#202")
booking_queue.enqueue("Ticket#203")

print("Oldest booking request:", booking_queue.front())
print("Processed booking:", booking_queue.dequeue())
print("Is booking queue empty?", booking_queue.is_empty())
