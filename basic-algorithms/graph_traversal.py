from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return visited


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

def main():
    # Sample graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # DFS traversal
    dfs_result = dfs(graph, 'A')
    print("DFS:", dfs_result)

    # BFS traversal
    bfs_result = bfs(graph, 'A')
    print("BFS:", bfs_result)

if __name__ == '__main__':
    main()
