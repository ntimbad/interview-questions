from collections import deque

def bidirectional_bfs(graph, start, end):
    if start not in graph or end not in graph:
        return False

    # Initialize the queues for the forward and backward search
    forward_queue = deque([start])
    backward_queue = deque([end])

    # Initialize the visited sets for the forward and backward search
    forward_visited = {start}
    backward_visited = {end}

    while forward_queue and backward_queue:
        # Forward step
        forward_current = forward_queue.popleft()
        for neighbor in graph[forward_current]:
            if neighbor in backward_visited:
                return True
            elif neighbor not in forward_visited:
                forward_visited.add(neighbor)
                forward_queue.append(neighbor)

        # Backward step
        backward_current = backward_queue.popleft()
        for neighbor in graph[backward_current]:
            if neighbor in forward_visited:
                return True
            elif neighbor not in backward_visited:
                backward_visited.add(neighbor)
                backward_queue.append(neighbor)

    # If the loop ends without returning, no path exists
    return False

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bidirectional_bfs(graph, 'A', 'F'))  # Output: True
print(bidirectional_bfs(graph, 'A', 'Z'))  # Output: False
