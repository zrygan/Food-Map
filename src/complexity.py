from imports import *
from graph import *
from ucs import *
from a_star import *
import random
import timeit
import matplotlib.pyplot as plt
import numpy as np


def create_graph(n_vertices: int, n_edges: int) -> Graph:
    def create_edge(
        u: int, v: int, edges: list[tuple[int, int]]
    ) -> tuple[tuple[int, int], float]:
        if u == v:
            return (-1, -1), -1
        if (u, v) not in edges and (v, u) not in edges:
            return (u, v), round(random.uniform(0.1, 10.0), 2)
        return (-1, -1), -1

    vertices = {}
    heuristics = {}

    for i in range(n_vertices):
        vertices[i] = "Node" + str(i)
        heuristics[i] = round(random.uniform(0.1, 10.0), 2)

    edges = []
    weights = []

    # each vertex has at least one edge
    while len(edges) < n_edges:
        u = random.randint(0, n_vertices - 1)
        v = random.randint(0, n_vertices - 1)

        if u != v:
            edge, weight = create_edge(u, v, edges)
            if weight != -1:
                edges.append(edge)
                weights.append(weight)

    # Create graph instance
    graph = Graph(len(edges), len(vertices))
    graph.make(vertices, edges)
    graph.give_weight(weights)
    graph.give_heuristic(heuristics)

    return graph


def run_ucs(graph, start_vertex, end_vertex):
    ucs(graph, start_vertex, end_vertex)


def run_a_star(graph, start_vertex, end_vertex):
    a_star(graph, start_vertex, end_vertex)


def run_dfs(graph, start_vertex, end_vertex):
    dfs(graph, start_vertex, set(), end_vertex)


def complex_ucs(rep, params) -> tuple[list[float], float]:
    time_complexity = []

    for key in params:
        n_vertices, n_edges = params[key]
        for _ in range(rep):
            graph = create_graph(n_vertices, n_edges)

            start_vertex = random.randint(0, n_vertices - 1)
            end_vertex = start_vertex
            while end_vertex == start_vertex:
                end_vertex = random.randint(0, n_vertices - 1)

            elapsed_time = timeit.timeit(
                lambda: run_ucs(graph, start_vertex, end_vertex), number=1
            )
            time_complexity.append((key, elapsed_time))

    return time_complexity, round(
        sum(t[1] for t in time_complexity) / (rep * len(params)), 10
    )


def complex_a_star(rep, params) -> tuple[list[float], float]:
    time_complexity = []

    for key in params:
        n_vertices, n_edges = params[key]
        for _ in range(rep):
            graph = create_graph(n_vertices, n_edges)

            start_vertex = random.randint(0, n_vertices - 1)
            end_vertex = start_vertex
            while end_vertex == start_vertex:
                end_vertex = random.randint(0, n_vertices - 1)

            elapsed_time = timeit.timeit(
                lambda: run_a_star(graph, start_vertex, end_vertex), number=1
            )
            time_complexity.append((key, elapsed_time))

    return time_complexity, round(
        sum(t[1] for t in time_complexity) / (rep * len(params)), 10
    )


def complex_dfs(rep, params) -> tuple[list[float], float]:
    time_complexity = []

    for key in params:
        n_vertices, n_edges = params[key]
        for _ in range(rep):
            graph = create_graph(n_vertices, n_edges)

            start_vertex = random.randint(0, n_vertices - 1)
            end_vertex = start_vertex
            while end_vertex == start_vertex:
                end_vertex = random.randint(0, n_vertices - 1)

            elapsed_time = timeit.timeit(
                lambda: run_dfs(graph, start_vertex, end_vertex), number=1
            )
            time_complexity.append((key, elapsed_time))

    return time_complexity, round(
        sum(t[1] for t in time_complexity) / (rep * len(params)), 10
    )


def runtime_v_test(
    a_star_data: list[tuple[int, float]],
    ucs_data: list[tuple[int, float]],
    dfs_data: list[tuple[int, float]],
    a_star_avg: float,
    ucs_avg: float,
    dfs_avg: float,
) -> None:
    a_star_keys, a_star_times = zip(*a_star_data)
    ucs_keys, ucs_times = zip(*ucs_data)
    dfs_keys, dfs_times = zip(*dfs_data)

    plt.figure(figsize=(10, 5))

    plt.scatter(a_star_keys, a_star_times, color="blue", label="A* Runtime", alpha=0.6)
    plt.scatter(ucs_keys, ucs_times, color="red", label="UCS Runtime", alpha=0.6)
    plt.scatter(dfs_keys, dfs_times, color="black", label="DFS Runtime", alpha=0.6)

    plt.axhline(y=a_star_avg, color="blue", linestyle="--", label="A* Average Time")
    plt.axhline(y=ucs_avg, color="red", linestyle="--", label="UCS Average Time")
    plt.axhline(y=dfs_avg, color="black", linestyle="--", label="DFS Average Time")

    plt.xticks(a_star_keys)
    plt.xlabel("Test #")
    plt.ylabel("Time (seconds)")
    plt.title("Runtime of A*, UCS, and DFS")
    plt.legend()
    plt.grid()
    plt.show()


def runtime_comparison(
    a_star_data: list[tuple[int, float]],
    ucs_data: list[tuple[int, float]],
    dfs_data: list[tuple[int, float]],
    n_data: int,
) -> None:
    _, a_star_times = zip(*a_star_data)
    _, ucs_times = zip(*ucs_data)
    _, dfs_times = zip(*dfs_data)

    plt.figure(figsize=(10, 5))
    
    x = range(1,n_data + 1)

    # A* data
    plt.scatter(x, a_star_times, color="blue", label="A* Runtime", alpha=0.6)
    a_star_fit = np.polyfit(x, a_star_times, 2)
    a_star_curve = np.polyval(a_star_fit, x)
    plt.plot(x, a_star_curve, color="blue", linestyle='--')

    # UCS data
    plt.scatter(x, ucs_times, color="red", label="UCS Runtime", alpha=0.6)
    ucs_fit = np.polyfit(x, ucs_times, 2)
    ucs_curve = np.polyval(ucs_fit, x)
    plt.plot(x, ucs_curve, color="red", linestyle='--')

    # DFS data
    plt.scatter(x, dfs_times, color="black", label="DFS Runtime", alpha=0.6)
    dfs_fit = np.polyfit(x, dfs_times, 2)
    dfs_curve = np.polyval(dfs_fit, x)
    plt.plot(x, dfs_curve, color="black", linestyle='--')
        
    # Adding labels and title
    plt.ylabel("Time (seconds)")
    plt.title("Runtime Comparison of A*, UCS, and DFS")
    plt.xticks([])
    plt.legend()
    plt.grid(False)

    plt.show()


if __name__ == "__main__":
    rep = 10            # how many times it will do that test case
    params = {          # Test cases, edges = n(n-1) / 2 
    1: [10, 15],        # 10 vertices, 15 edges
    2: [15, 20],        # 15 vertices, 20 edges
    3: [15, 50],        # 15 vertices, 50 edges
    4: [20, 40],        # 20 vertices, 40 edges
    5: [20, 80],        # 20 vertices, 80 edges
    6: [25, 60],        # 25 vertices, 60 edges
    7: [25, 90],        # 25 vertices, 90 edges
    8: [30, 90],        # 30 vertices, 90 edges
    9: [30, 120],       # 30 vertices, 120 edges
    10: [35, 100],      # 35 vertices, 100 edges
    11: [40, 150],      # 40 vertices, 150 edges
    12: [40, 780],      # 40 vertices, 780 edges
    13: [45, 180],      # 45 vertices, 180 edges
    14: [50, 200],      # 50 vertices, 200 edges
    15: [60, 300],      # 60 vertices, 300 edges
    }

    a_star_data, a_star_ave = complex_a_star(rep, params)
    ucs_data, ucs_ave = complex_ucs(rep, params)
    dfs_data, dfs_ave = complex_dfs(rep, params)

    runtime_v_test(a_star_data, ucs_data, dfs_data, a_star_ave, ucs_ave, dfs_ave)
    runtime_comparison(a_star_data, ucs_data, dfs_data, rep * len(params))
