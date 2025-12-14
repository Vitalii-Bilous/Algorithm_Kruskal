import matplotlib.pyplot as plt
import csv
import numpy as np

def data_from_csv(filename, density):
    x_n = []
    y_time = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        data = []
        for line in reader:
            n = int(line["n"])
            dens = float(line["density"])
            time = float(line["avg_time"])
            if round(dens, 1) == round(density, 1):
                data.append((n, time))

        data.sort(key=lambda x: x[0])
        for n, time in data:
            x_n.append(n)
            y_time.append(time)
        return x_n, y_time

def analysis_experiments(matrix_file, list_file, density):
    data_matrix = data_from_csv(matrix_file, density)
    data_list = data_from_csv(list_file, density)

    n_matrix = data_matrix[0]
    time_matrix = data_matrix[1]

    n_list = data_list[0]
    time_list = data_list[1]

    plt.figure(figsize=(8,8))
    plt.plot(n_matrix, time_matrix, label= "Adjacency Matrix", color="#7600BC", marker="o")
    plt.plot(n_list, time_list, label="Adjacency List", color="#E3256B", marker="s")

    plt.title(f"Робота алгоритму Крускала(density = {density})")
    plt.xlabel("Кількість вершин(n)")
    plt.ylabel("Середній час(с)")
    plt.grid(True, axis="y", alpha=0.4)
    plt.legend()
    plt.yscale("log")
    plt.tight_layout()
    name = f"Visual/time_n_{density}.png"
    plt.savefig(name, dpi=300)
    plt.close()

def bar_charts(density):
     w = 0.4
     data_matrix = data_from_csv("results_adjacency_matrix.csv", density)
     data_list = data_from_csv("results_adjacency_list.csv", density)

     n_matrix = data_matrix[0]
     time_matrix = data_matrix[1]

     n_list = data_list[0]
     time_list = data_list[1]

     x = np.arange(len(n_list))
     plt.figure(figsize=(10, 10))
     plt.bar(x + w/2, time_matrix, width=w, color="#7600BC",  label="results_adjacency_matrix")
     plt.bar(x - w/2, time_list, width=w, color="#E3256B", label="results_adjacency_list")

     plt.title(f"Adjacency list vs Adjacency matrix (density = {density})")
     plt.xlabel("Кількість вершин(n)")
     plt.ylabel("Середній час(с)")
     plt.grid(True, axis="y", alpha=0.4)
     plt.xticks(x, n_list)
     plt.legend()
     plt.tight_layout()
     name = f"Visual/Adjacency_list_vs_Adjacency_matrix_{density}.png"
     plt.savefig(name, dpi=300)
     plt.close()

if __name__ == "__main__":
    densities = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for d in densities:
        analysis_experiments("results_adjacency_matrix.csv", "results_adjacency_list.csv", density=d)
        bar_charts(d)
