graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": [],
    "F": ["H"],
    "G": [],
    "H": []
}

def dfs(graph, root, visited):
    visited.add(root)
    print(root)
    for neighbor in graph[root]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

visited = set()
dfs(graph, "A", visited)