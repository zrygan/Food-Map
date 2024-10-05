# main
# contains the main function for the project

from imports import *
from graph import *

if __name__ == "__main__":
    """ the following variables can be changed for tesitng
    """
    start_index = "A"
    goal_index = "A"
    
    # a dictionary of the restaurant and their single-letter equivalent
    # since this is a dictionary we cannot use numerical indices to access each vertex
    # we can instead use the ASCII equivalent of each alphabetical characher
    # example:      vertices[chr(65)] == "University Mall"
    #               A in ASCII is thr 65th character
    vertices = {
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

    # idk how the edges work, but ill make this for now
    edges = [
    ("U", "J"),
    ("J", "K"),
    ("J", "L"),
    ("H", "L"),
    ("J", "I"),
    ("I", "N"),
    ("N", "M"),
    ("I", "G"),
    ("G", "F"),
    ("F", "E"),
    ("E", "D"),
    ("E", "O"),
    ("O", "S"),
    ("S", "P"),
    ("O", "P"),
    ("P", "Q"),
    ("Q", "R"),
    ("R", "T"),
    ("T", "A"),
    ("A", "B"),
    ("B", "C"),
    ("C", "A"),
    # Adding reciprocal edges
    # this can be removed, if unecessary (just here if needed) - zhean
    ("J", "U"),
    ("K", "J"),
    ("L", "J"),
    ("L", "H"),
    ("I", "J"),
    ("N", "I"),
    ("M", "N"),
    ("G", "I"),
    ("F", "G"),
    ("E", "F"),
    ("D", "E"),
    ("O", "E"),
    ("S", "O"),
    ("P", "S"),
    ("P", "O"),
    ("Q", "P"),
    ("R", "Q"),
    ("T", "R"),
    ("A", "T"),
    ("B", "A"),
    ("C", "B"),
    ("A", "C")]
        
    # an array of edge weights of each edge
    # len(weights) == len(edges)    => each edge must have a weight if at least one edge has
    weights = []

    # an array of the heuristics of each node
    # len(heuristics) == len(vertices)    => each node must have a heuristic if at least one node has
    heuristics = []

    start_node = vertices[start_index]
    # goal_node = edges[goal_index] #FIXME: this is an error since edges is NOT a dict, it is a list/array

    graph = Graph(len(edges), len(vertices))
    graph.make(vertices, edges)
    graph.give_weight(weights)          # we can keep this even if the weight array is empty
    graph.give_heuristic(heuristics)    # same for this
    graph.view()

    print("Done")
