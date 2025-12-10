from collections import deque, defaultdict

def bfs_traversal(graph, root):
    ans = []
    visited = set([root])
    queue = deque([root])
    while queue:
        node = queue.popleft()
        ans.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return ans

def bfs_layers(graph, root):
    layers = defaultdict(list)
    visited = set([root])
    queue = deque([(root, 0)])
    while queue:
        node, layer = queue.popleft()
        layers[layer].append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, layer + 1))
    return [layer for _, layer in layers.items()]

def bfs_layers_simpler(graph, root):
    layers = []
    visited = set([root])
    queue = deque([(root, 0)])
    while queue:
        node, layer = queue.popleft()
        if layer >= len(layers):
            layers.append([])
        layers[layer].append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, layer + 1))
    return layers

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

print(bfs_traversal(graph, "A"))
print(bfs_layers(graph, "A"))
print("layers simplified works as well: ", bfs_layers(graph, "A") == bfs_layers_simpler(graph, "A"))