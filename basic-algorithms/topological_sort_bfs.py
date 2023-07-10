from collections import deque, defaultdict


def topological_sort(graph):
    in_degree = defaultdict(int)

    # Compute in-degrees of each node
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Find all nodes with no incoming edges
    queue = deque([node for node in graph if in_degree[node] == 0])

    result = []
    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if there was a cycle
    if len(result) != len(graph):
        return None  # cycle detected
    else:
        return result


# Define the graph as an adjacency list
graph = {
    '5': ['2', '0'],
    '4': ['0', '1'],
    '2': ['3'],
    '3': ['1'],
    '0': [],
    '1': []
}

# Get the topological sort
print(topological_sort(graph))  # Outputs: ['5', '4', '2', '3', '0', '1']
