from imports import *
from graph import *
from ucs import *
from a_star import *
import random
import timeit
import matplotlib.pyplot as plt  # Ensure you import matplotlib for plotting

def create_graph(n_vertices: int, n_edges: int) -> Graph:
    def create_edge(u: int, v: int, edges: list[tuple[int, int]]) -> tuple[tuple[int, int], float]:
        if u == v:
            return (-1, -1), -1  # Avoid self-loops
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
    
    # Ensure that each vertex has at least one edge
    while len(edges) < n_edges:
        u = random.randint(0, n_vertices - 1)
        v = random.randint(0, n_vertices - 1)
        
        if u != v:  # Avoid self-loops
            edge, weight = create_edge(u, v, edges)
            if weight != -1:  # Valid edge
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

            elapsed_time = timeit.timeit(lambda: run_ucs(graph, start_vertex, end_vertex), number=1)
            time_complexity.append((key, elapsed_time))  # Store key and elapsed time

    return time_complexity, round(sum(t[1] for t in time_complexity) / (rep * len(params)), 10)

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

            elapsed_time = timeit.timeit(lambda: run_a_star(graph, start_vertex, end_vertex), number=1)
            time_complexity.append((key, elapsed_time))  # Store key and elapsed time
            
    return time_complexity, round(sum(t[1] for t in time_complexity) / (rep * len(params)), 10)

def plot(a_star_data: list[tuple[int, float]], ucs_data: list[tuple[int, float]]) -> None:
    a_star_keys, a_star_times = zip(*a_star_data)
    ucs_keys, ucs_times = zip(*ucs_data)
    
    plt.figure(figsize=(10, 5))
    
    plt.scatter(a_star_keys, a_star_times, color='blue', label='A* Runtime', alpha=0.6)
    plt.scatter(ucs_keys, ucs_times, color='red', label='UCS Runtime', alpha=0.6)
    
    plt.xticks(a_star_keys)  # Show x-ticks for each parameter set
    plt.xlabel('Test #')
    plt.ylabel('Time (seconds)')
    plt.title('Runtime of A* vs UCS')
    plt.legend()
    plt.grid()
    plt.show()
    

if __name__ == "__main__":
    rep = 10  # You can adjust this for fewer repetitions if needed
    params = {
        1: [20, 100],
        2: [30, 200],
        3: [40, 300],
        4: [50, 400],
        5: [60, 500],
        # Add more as needed
    }
    
    a_star_data, a_star_ave = complex_a_star(rep, params)
    ucs_data, ucs_ave = complex_ucs(rep, params)
    
    print("A* Average Time:", a_star_ave)
    print("UCS Average Time:", ucs_ave)
    plot(a_star_data, ucs_data)
