class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_traversal(root):
    stack = []
    current = root

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end=" ")

        current = current.right


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(7)

print("Inorder Traversal:")
inorder_traversal(root)
