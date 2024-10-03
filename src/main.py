# main
# contains the main function for the project

from imports import *
from graph import *

if __name__ == "__main__":
    """ the following variables can be changed for tesitng
    """
    start_vertex = "A"
    goal_vertex = "A"
    
    restos = {
        "A": "University Mall",
        "B": "Mcdonald's",
        "C": "Perico's",
        "D": "Bloemen Hall",
        "E": "W.H Taft Residence",
        "F": "EGI Taft",
        "G": "Castro Street",
        "H": "One Archer's",
        "J": "La Casita",
        "K": "Green Mall",
        "L": "Green Court",
        "M": "Sherwood",
        "N": "Jolibee",
        "O": "Dagonoy St.",
        "P": "Burgundy",
        "Q": "Estrada St.",
        "R": "D' Student's Place",
        "S": "Leon Guinto St.",
        "T": "P. Ocampo St.",
        "U": "Fidel A. Reyes St.",
    }

    """ the following variables CANNOT be changed
    """
    vertex = []
    edges = []
    weights = []
    heuristics = {}

    n_edges = 0
    n_vertices = 0

    start = restos[start_vertex]
    goal = restos[goal_vertex]

    for resto in restos:
        vertex.append(resto)
        n_edges += 1

    graph = Graph(n_edges, n_vertices)
    graph.make(vertex, edges)
    graph.give_weight(weights)
    graph.give_heuristic(heuristics)
    graph.view()

    print("Done")
