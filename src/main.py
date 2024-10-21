# main
# contains the main function for the project

from graph import *

if __name__ == "__main__":
    """ the following variables can be changed for tesitng
    """
    start_index = 1
    goal_index = 1
    
    # a dictionary of the restaurant and their single-letter equivalent
    # since this is a dictionary we cannot use numerical indices to access each vertex
    # we can instead use the ASCII equivalent of each alphabetical characher
    # example:      vertices[chr(65)] == "University Mall"
    #               A in ASCII is thr 65th character
    # Updated vertices with numbers
    vertices = {
        1: "University Mall",
        2: "Mcdonald's",
        3: "Perico's",
        4: "Bloemen Hall",
        5: "W.H Taft Residence",
        6: "EGI Taft",
        7: "Castro Street",
        8: "Agno Food Court",
        9: "One Archers'",
        10: "La Casita",
        11: "Green Mall",
        12: "Green Court",
        13: "Sherwood",
        14: "Jolibee",
        15: "Dagonoy St.",
        16: "Burgundy",
        17: "Estrada St.",
        18: "D' Student's Place",
        19: "Leon Guinto St.",
        20: "P. Ocampo St.",
        21: "Fidel A. Reyes St.",
    }

    # Updated edges with numbers
    edges = [
        (21, 10),
        (10, 11),
        (10, 12),
        (8, 12),
        (10, 9),
        (9, 14),
        (14, 13),
        (9, 7),
        (7, 6),
        (6, 5),
        (5, 4),
        (5, 15),
        (15, 19),
        (19, 16),
        (15, 16),
        (16, 17),
        (17, 18),
        (18, 20),
        (20, 1),
        (1, 2),
        (2, 3),
        (3, 1)
    ]
            
    # an array of edge weights of each edge
    # len(weights) == len(edges)    => each edge must have a weight if at least one edge has
    weights = []

    # an array of the heuristics of each node
    # len(heuristics) == len(vertices)    => each node must have a heuristic if at least one node has
    heuristics = []

    start_node = vertices[start_index]
    goal_node = edges[goal_index] 

    graph = Graph(len(edges), len(vertices))
    graph.make(vertices, edges)
    graph.give_weight(weights)
    graph.give_heuristic(heuristics)
    # graph.remove_edge((2,3))
    graph.view() 