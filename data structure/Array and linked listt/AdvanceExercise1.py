class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reversegroup(head, k):
    curr = head
    count = 0

    while curr and count < k:
        curr = curr.next
        count += 1

    if count < k:
        return head

    prev = None
    curr = head
    next_node = None
    count = 0

    while curr and count < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count += 1

    head.next = reversegroup(curr, k)
    return prev

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

k = 2
head = reversegroup(head, k)
print_list(head)
