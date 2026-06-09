def has_cycle_dfs(graph):
    visited = set()
    recStack = set()

    def dfs(node):
        visited.add(node)
        recStack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in recStack:
                return True

        recStack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [1],
    4: []
}

print("Cycle Exists:", has_cycle_dfs(graph))
