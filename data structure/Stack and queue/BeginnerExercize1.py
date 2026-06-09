stack = []
def insert_at_bottom(x):
    if len(stack) == 0:
        stack.append(x)
        return

    temp = stack.pop()
    insert_at_bottom(x)
    stack.append(temp)

def reverse_stack():
    if len(stack) == 0:
        return

    temp = stack.pop()
    reverse_stack()
    insert_at_bottom(temp)

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print("Original Stack:", stack)

reverse_stack()

print("Reversed Stack:", stack)
