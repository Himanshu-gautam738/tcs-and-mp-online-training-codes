from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            self.add_vertex(v1)
        if v2 not in self.graph:
            self.add_vertex(v2)

        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def display(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        print("BFS Traversal:", end=" ")

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

    def dfs(self, start):
        visited = set()
        print("DFS Traversal:", end=" ")
        self._dfs_helper(start, visited)
        print()

    def _dfs_helper(self, node, visited):
        visited.add(node)
        print(node, end=" ")

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)

g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")

print("Graph:")
g.display()

g.bfs("A")
g.dfs("A")
