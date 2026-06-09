from collections import deque

def interleave_queue(queue):
    stack = []
    n = len(queue)

    for _ in range(n // 2):
        stack.append(queue.popleft())

    while stack:
        queue.append(stack.pop())

    for _ in range(n // 2):
        queue.append(queue.popleft())

    for _ in range(n // 2):
        stack.append(queue.popleft())

    while stack:
        queue.append(stack.pop())
        queue.append(queue.popleft())

q = deque([1, 2, 3, 4, 5, 6])
interleave_queue(q)
print("Interleaved Queue:", list(q))
