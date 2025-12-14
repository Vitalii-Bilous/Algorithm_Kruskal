import random

class Graph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.adjacency_list = {x: [] for x in range(num_vertices)}
        self.edges = []

    def add_edge(self, u, v, weight):
        if not (0 <= u < self.num_vertices and 0 <= v < self.num_vertices):
            raise ValueError("Vertex index is out of range")
        if u == v:
            raise ValueError("Self-loops are not needed")
        if self.adjacency_matrix[u][v] != 0:
            raise ValueError("The edge already exists")

        self.adjacency_matrix[u][v] = weight
        self.adjacency_matrix[v][u] = weight
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))
        self.edges.append((u, v, weight))

    def matrix_to_edges(self):
        self.edges = []
        for u in range(self.num_vertices):
            for v in range(u + 1, self.num_vertices):
                weight = self.adjacency_matrix[u][v]
                if weight != 0:
                    self.edges.append((u, v, weight))

    def list_to_edges(self):
        self.edges = []
        for u, n in self.adjacency_list.items():
            for v, weight in n:
                if u < v:
                    self.edges.append((u, v, weight))

    def dfs(self, vertices, visited):
        visited[vertices] = True
        for n, w in self.adjacency_list[vertices]:
            if not visited[n]:
                self.dfs(n, visited)

    def connected(self):
        visited = [False] * self.num_vertices
        self.dfs(0, visited)
        return all(visited)

def generate_random_graph(num_vertices, density):
    if not 0 <= density <= 1:
        raise ValueError("Density must be between 0 and 1")
    while True:
        g = Graph( num_vertices)
        max_edges = ( num_vertices * ( num_vertices - 1)) // 2
        needed_edges = int(max_edges * density)
        edges_created = 0

        while edges_created < needed_edges:
            u = random.randint(0, num_vertices - 1)
            v = random.randint(0, num_vertices - 1)
            weight = random.randint(1, 100)
            if u != v and g.adjacency_matrix[u][v] == 0:
                g.add_edge(u, v, weight)
                edges_created += 1
        if g.connected():
            return g