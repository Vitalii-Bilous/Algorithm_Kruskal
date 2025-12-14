class DSU:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, u, v):
        main_u = self.find(u)
        main_v = self.find(v)
        if main_u == main_v:
            return False
        if self.rank[main_u] < self.rank[main_v]:
            self.parent[main_u] = main_v
        elif self.rank[main_v] < self.rank[main_u]:
            self.parent[main_v] = main_u
        else:
            self.parent[main_v] = main_u
            self.rank[main_u] += 1
        return True
