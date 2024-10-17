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
        "S",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
    ]

    # idk how the edges work, but ill make this for now
    edges = [
        ("S", "A"), ("S", "D"),
        ("A", "D"), ("A", "B"),
        ("B", "C"), ("B", "E"),
        ("D", "E"),
        ("E", "F"),
        ("F", "G"),

        ("A", "S"), ("D", "S"),
        ("D", "A"), ("B", "A"),
        ("C", "B"), ("E", "B"),
        ("E", "D"),
        ("F", "E"),
        ("G", "F")
    ]

    # an array of edge weights of each edge
    # len(weights) == len(edges)    => each edge must have a weight if at least one edge has
    weights = [2, 5, 2, 1, 4, 5, 2, 4, 3,
               2, 5, 2, 1, 4, 5, 2, 4, 3]

    # an array of the heuristics of each node
    # len(heuristics) == len(vertices)    => each node must have a heuristic if at least one node has
    heuristics = {
        "S": 11.0,
        "A": 10.4,
        "B": 6.7,
        "C": 4.0,
        "D": 8.9,
        "E": 6.9,
        "F": 3.0,
        "G": 0
    }

    start_node = "S"
    goal_node = ["G"]

    graph = Graph(len(edges), len(vertices))
    graph.make(vertices, edges)
    graph.give_weight(weights)          # we can keep this even if the weight array is empty
    graph.give_heuristic(heuristics)    # same for this

    a_star_result = a.a_star(graph, start_node, goal_node)
    print("Expected Path: ['S', 'A', 'D', 'E', 'F', 'G'] \nExpected Cost: 13\n")

    print("A*")
    print("Path: ", a_star_result[0], "\nCost: ", a_star_result[1])
    graph.view()


    print("Done")
