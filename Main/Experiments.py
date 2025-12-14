from Graph import generate_random_graph
from Kruskal import kruskal
import time
import csv

def experiments():
    num_vertices = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
    density = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    num_repeat = 100
    results_adjacency_matrix = []
    results_adjacency_list= []

    for n in num_vertices:
        for d in density:
            graphs = []
            for _ in range(num_repeat):
                g = generate_random_graph(n, d)
                graphs.append(g)

            times_matrix = []
            for g in graphs:
                start_time = time.perf_counter()
                g.matrix_to_edges()
                kruskal(g)
                end_time = time.perf_counter()
                absolute_time = end_time - start_time
                times_matrix.append(absolute_time)
            avg_time_matrix = sum(times_matrix) / len(times_matrix)
            results_adjacency_matrix.append((n, d, avg_time_matrix))

            times_list = []
            for g in graphs:
                start_time = time.perf_counter()
                g.list_to_edges()
                kruskal(g)
                end_time = time.perf_counter()
                absolute_time = end_time - start_time
                times_list.append(absolute_time)
            avg_time_list = sum(times_list) / len(times_list)
            results_adjacency_list.append((n, d, avg_time_list))
    return results_adjacency_matrix, results_adjacency_list

def print_experiments(name, result):
    line = "+" + "-" * 9 + "+" + "-" * 11 + "+" + "-" * 18 + "+"
    print("\n" + name)
    print(line)
    print(f"| {'n':^7} | {'density':^9} | {'average time':^16} |")
    print(line)
    for n, d, avg in result:
        print(f"| {n:^7} | {d:^9.2f} | {avg:^16.8f} |")
    print(line)

def save_to_csv(results_adjacency_matrix, results_adjacency_list):
    with open("results_adjacency_matrix.csv", "w", newline="") as csvfile:
        fieldnames = ["n", "density", "avg_time"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for n, d, avg in results_adjacency_matrix:
            writer.writerow({"n": n, "density": d, "avg_time": f"{avg:.10f}"})

    with open("results_adjacency_list.csv", "w", newline="") as csvfile:
        fieldnames = ["n", "density", "avg_time"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for n, d, avg in results_adjacency_list:
            writer.writerow({"n": n, "density": d, "avg_time": f"{avg:.10f}"})

if __name__ == "__main__":
    results_adjacency_matrix, results_adjacency_list = experiments()
    print_experiments("Adjacency matrix:", results_adjacency_matrix)
    print_experiments("Adjacency list:", results_adjacency_list)
    save_to_csv(results_adjacency_matrix, results_adjacency_list)
