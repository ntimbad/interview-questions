from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self, num_vertices):
        self.graph = defaultdict(list)
        self.num_vertices = num_vertices

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def topological_sort_util(self, node, visited, recursion_stack, result):
        visited[node] = True
        recursion_stack[node] = True

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                if self.topological_sort_util(neighbor, visited, recursion_stack, result):
                    return True
            elif recursion_stack[neighbor]:
                return True

        result.appendleft(node)
        recursion_stack[node] = False
        return False

    def topological_sort(self):
        visited = [False] * self.num_vertices
        recursion_stack = [False] * self.num_vertices
        result = deque()

        for node in range(self.num_vertices):
            if not visited[node]:
                if self.topological_sort_util(node, visited, recursion_stack, result):
                    return None  # Return None if a cycle is detected

        return list(result)

g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print(g.topological_sort())  # Outputs: [5, 4, 2, 3, 1, 0]
