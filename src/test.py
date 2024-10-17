# main
# contains the main function for the project

from imports import *
from graph import *
import a_star as a

if __name__ == "__main__":
    """ the following variables can be changed for tesitng
    """
    start_index = "A"
    goal_index = "A"

    vertices = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J"
    ]

    # idk how the edges work, but ill make this for now
    edges = [("A", "B"), ("A", "F"),
             ("B", "C"), ("B", "D"),
             ("C", "D"), ("C", "E"),
             ("D", "E"),
             ("E", "I"), ("E", "J"),
             ("F", "G"), ("F", "H"),
             ("G", "I"),
             ("H", "I"),
             ("I", "J"),

             ("B", "A"), ("F", "A"),
             ("C", "B"), ("D", "B"),
             ("D", "C"), ("E", "C"),
             ("E", "D"),
             ("I", "E"), ("J", "E"),
             ("G", "F"), ("H", "F"),
             ("I", "G"),
             ("I", "H"),
             ("J", "I")
             ]

    # an array of edge weights of each edge
    # len(weights) == len(edges)    => each edge must have a weight if at least one edge has
    weights = [6, 3, 3, 2, 1, 5, 8, 5, 5, 1, 7, 3, 2, 3,
               6, 3, 3, 2, 1, 5, 8, 5, 5, 1, 7, 3, 2, 3]

    # an array of the heuristics of each node
    # len(heuristics) == len(vertices)    => each node must have a heuristic if at least one node has
    heuristics = {
        "A": 10,
        "B": 8,
        "C": 5,
        "D": 7,
        "E": 3,
        "F": 6,
        "G": 5,
        "H": 3,
        "I": 1,
        "J": 0
    }

    start_node = "A"
    goal_node = ["J"]

    graph = Graph(len(edges), len(vertices))
    graph.make(vertices, edges)
    graph.give_weight(weights)          # we can keep this even if the weight array is empty
    graph.give_heuristic(heuristics)    # same for this

    a_star_result = a.a_star(graph, start_node, goal_node)
    print("Expected Path: ['A', 'F', 'G', 'I', 'J']\nExpected Cost: 10\n")
    print("A*")
    print("Path: ", a_star_result[0], "\nCost: ", a_star_result[1])
    graph.view()


    print("Done")
