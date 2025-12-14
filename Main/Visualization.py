import matplotlib.pyplot as plt
import networkx as nx
from Graph import generate_random_graph
from Kruskal import kruskal

def visual_graph(graph, file="Graph.png"):
    G = nx.Graph()
    for v in range(graph.num_vertices):
        G.add_node(v)
    for u, v, weight in graph.edges:
        G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G, seed=8)
    plt.figure(figsize=(8,8))

    nx.draw_networkx_nodes(G, pos, node_color="#8C0B0B", node_size=600, edgecolors="#400A0A", linewidths=2)
    nx.draw_networkx_edges(G, pos, edge_color="#D92323", width=3)
    nx.draw_networkx_labels(G, pos, font_size=10, font_color="white", font_weight="bold")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="#400A0A", font_size=12)

    plt.tight_layout()
    plt.savefig(file, dpi=300)
    plt.close()


def visual_kruskal(graph, mst_edges, file="Kruskal.png"):
    G = nx.Graph()
    for v in range(graph.num_vertices):
        G.add_node(v)
    for u, v, weight in graph.edges:
        G.add_edge(u, v, weight=weight)

    mst = []
    for u, v, weight in mst_edges:
        mst.append((u, v))
        mst.append((v, u))
    needed_edges = [(u, v) for u, v, weight in graph.edges
                    if tuple(sorted((u, v))) in mst]
    default_edges = [(u, v) for u, v, weight in graph.edges
                    if tuple(sorted((u, v))) not in mst]

    pos = nx.spring_layout(G, seed=8)
    plt.figure(figsize=(8, 8))

    nx.draw_networkx_nodes(G, pos, node_color="#8C0B0B", node_size=600, edgecolors="#400A0A", linewidths=2)
    nx.draw_networkx_edges(G, pos, edgelist=default_edges, edge_color="#88898C", width=1, style="dashed")
    nx.draw_networkx_edges(G, pos, edgelist=needed_edges, edge_color="#D92323", width=4, style="solid")
    nx.draw_networkx_labels(G, pos, font_size=10, font_color="white", font_weight="bold")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="#400A0A", font_size=8)

    plt.tight_layout()
    plt.savefig(file, dpi=300)
    plt.close()


if __name__ == "__main__":
    g = generate_random_graph(20, 0.3)
    visual_graph(g, file="Visual/graph.visual.png")
    mst_edges = kruskal(g)
    visual_kruskal(g, mst_edges, file="Visual/Kruskal.png")


