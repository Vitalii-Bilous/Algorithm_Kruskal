from DSU import DSU

def kruskal(graph):
    num = graph.num_vertices
    dsu = DSU(num)
    mst_edges = []
    edges = graph.edges
    sorted_edges = sorted(edges, key=lambda x: x[2])
    for u, v, weight in sorted_edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            if len(mst_edges) == num - 1:
                break
    return mst_edges




