class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    seen = set()
    curr = head
    prev = None

    while curr:
        if curr.data in seen:
            prev.next = curr.next
        else:
            seen.add(curr.data)
            prev = curr
        curr = curr.next
    return head
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(3)

head = remove_duplicates(head)
print_list(head)
