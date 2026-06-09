class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if root.data == p or root.data == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right

root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

p, q = 7, 4
lca = lowest_common_ancestor(root, p, q)
print("LCA:", lca.data)
