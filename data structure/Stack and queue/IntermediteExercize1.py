class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


def sort_stack(stackA):
    stackB = Stack()

    while not stackA.is_empty():
        temp = stackA.pop()

        while not stackB.is_empty() and stackB.peek() > temp:
            stackA.push(stackB.pop())

        stackB.push(temp)

    # Move back to stackA so that stackA is sorted
    while not stackB.is_empty():
        stackA.push(stackB.pop())


# Driver code
stackA = Stack()
for x in [3, 1, 4, 2]:
    stackA.push(x)

print("Original Stack A:", stackA)
sort_stack(stackA)
print("Sorted Stack A:", stackA)
