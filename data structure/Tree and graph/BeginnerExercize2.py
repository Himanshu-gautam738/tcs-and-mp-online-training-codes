from collections import deque

def bfs_shortest_path(graph, start, end):
    if start not in graph or end not in graph:
        return []

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        node = queue.popleft()
        if node == end:
            break
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    if end not in parent:
        return []

    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = parent[curr]

    return path[::-1]
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs_shortest_path(graph, 'A', 'F'))
