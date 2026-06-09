import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)

        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def display(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

    def dijkstra(self, source):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[source] = 0

        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

g = Graph()

g.add_edge("A", "B", 4)
g.add_edge("A", "C", 1)
g.add_edge("C", "B", 2)
g.add_edge("B", "D", 1)
g.add_edge("C", "D", 5)
g.add_edge("D", "E", 3)

print("Graph:")
g.display()

source = "A"
shortest_paths = g.dijkstra(source)

print("\nShortest distances from source:", source)
for vertex in shortest_paths:
    print(vertex, ":", shortest_paths[vertex])
