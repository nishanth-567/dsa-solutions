from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def display(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.adj_list[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


graph = Graph()

vertices = input("Enter the vertices separated by space: ").split()

num_edges = int(input("Enter number of edges: "))
for i in range(num_edges):
    v1, v2 = input(f"Enter edge {i+1} (e.g. A B): ").split()
    graph.add_edge(v1, v2)

print("\nAdjacency List Representation:")
graph.display()

start = input("\nEnter starting vertex for DFS: ")
print("Depth-First Search Traversal:")
graph.dfs(start)
print()

start = input("\nEnter starting vertex for BFS: ")
print("Breadth-First Search Traversal:")
graph.bfs(start)
print()
