def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)
    print("Exploring node:", start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


graph = {}
n = int(input("How many edges? "))

for i in range(n):
    u, v = input("Enter edge (e.g., A B): ").split()

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)

start = input("Enter starting node: ")

print("DFS Traversal:")
dfs(graph, start)