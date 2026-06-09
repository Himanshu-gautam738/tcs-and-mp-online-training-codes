from typing import TypeVar, Generic

# Generic type variable
T = TypeVar('T')

# Generic Set Class
class GenericSet(Generic[T]):
    def __init__(self):
        self._items: set[T] = set()

    def add(self, item: T) -> None:
        """Add an element to the set if not already present."""
        if item in self._items:
            print(f"{item} already exists in the set.")
        else:
            self._items.add(item)
            print(f"Added: {item}")

    def remove(self, item: T) -> None:
        """Remove an element from the set if it exists."""
        if item in self._items:
            self._items.remove(item)
            print(f"Removed: {item}")
        else:
            print(f"{item} does not exist in the set.")

    def contains(self, item: T) -> bool:
        """Check if the element is in the set."""
        return item in self._items

    def display(self) -> None:
        """Display all elements in the set."""
        print("Set elements:", self._items)

# === Testing the GenericSet ===
if __name__ == "__main__":
    # Integer Set
    int_set = GenericSet[int]()
    int_set.add(10)
    int_set.add(20)
    int_set.add(10)  # duplicate
    int_set.display()
    int_set.remove(20)
    int_set.remove(30)  # non-existent
    print("Contains 10?", int_set.contains(10))
    print("Contains 20?", int_set.contains(20))

    print("\n--- String Set ---")
    str_set = GenericSet[str]()
    str_set.add("apple")
    str_set.add("banana")
    str_set.add("apple")  # duplicate
    str_set.display()
    str_set.remove("banana")
    print("Contains 'apple'?", str_set.contains("apple"))
    print("Contains 'banana'?", str_set.contains("banana"))

    print("\n--- Float Set ---")
    float_set = GenericSet[float]()
    float_set.add(3.14)
    float_set.add(2.718)
    float_set.add(3.14)  # duplicate
    float_set.display()
    float_set.remove(3.14)
    print("Contains 3.14?", float_set.contains(3.14))
    print("Contains 2.718?", float_set.contains(2.718))
