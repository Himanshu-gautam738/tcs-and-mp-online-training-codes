class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_dll(arr):
    head = DNode(arr[0])
    curr = head
    for i in arr[1:]:
        new = DNode(i)
        curr.next = new
        new.prev = curr
        curr = new
    return head

def dll_insert_begin(head, data):
    new = DNode(data)
    new.next = head
    head.prev = new
    return new

def dll_delete(head, key):
    curr = head
    while curr:
        if curr.data == key:
            if curr.prev:
                curr.prev.next = curr.next
            else:
                head = curr.next
            if curr.next:
                curr.next.prev = curr.prev
            break
        curr = curr.next
    return head

def print_dll(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()


def create_cll(arr):
    head = CNode(arr[0])
    curr = head
    for i in arr[1:]:
        new = CNode(i)
        curr.next = new
        curr = new
    curr.next = head
    return head

def cll_insert_begin(head, data):
    new = CNode(data)
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = new
    new.next = head
    return new

def cll_delete(head, key):
    curr = head
    prev = None
    while True:
        if curr.data == key:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next
        if curr == head:
            break
    return head

def print_cll(head):
    curr = head
    while True:
        print(curr.data, end=" ")
        curr = curr.next
        if curr == head:
            break
    print()


arr = [5, 15, 25, 35]

dll = create_dll(arr)
dll = dll_insert_begin(dll, 20)
dll = dll_delete(dll, 25)
print_dll(dll)

cll = create_cll(arr)
cll = cll_insert_begin(cll, 20)
cll = cll_delete(cll, 25)
print_cll(cll)
