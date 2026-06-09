from typing import TypeVar, Generic, List

# Type variable for generic queue
T = TypeVar('T')

# Generic Queue Class
class Queue(Generic[T]):
    def __init__(self):
        self._items: List[T] = []

    def enqueue(self, item: T) -> None:
        """Add an element to the rear of the queue."""
        self._items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self) -> T:
        """Remove and return the front element of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self._items.pop(0)
        print(f"Dequeued: {item}")
        return item

    def front(self) -> T:
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Front called on empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._items) == 0

# === Testing the Queue ===
if __name__ == "__main__":
    # Queue of integers
    int_queue = Queue[int]()
    int_queue.enqueue(10)
    int_queue.enqueue(20)
    int_queue.enqueue(30)
    print(f"Front element: {int_queue.front()}")
    int_queue.dequeue()
    print(f"Is queue empty? {int_queue.is_empty()}")

    print("\n--- String Queue ---")
    # Queue of strings
    str_queue = Queue[str]()
    str_queue.enqueue("apple")
    str_queue.enqueue("banana")
    print(f"Front element: {str_queue.front()}")
    str_queue.dequeue()
    print(f"Is queue empty? {str_queue.is_empty()}")

    print("\n--- Float Queue ---")
    # Queue of floats
    float_queue = Queue[float]()
    float_queue.enqueue(3.14)
    float_queue.enqueue(2.718)
    print(f"Front element: {float_queue.front()}")
    float_queue.dequeue()
    float_queue.dequeue()
    print(f"Is queue empty? {float_queue.is_empty()}")
