# main
# contains the main function for the project

from imports import *
from graph import *
import a_star as a
import ucs as u

if __name__ == "__main__":
    """ the following variables can be changed for tesitng
    """
    start_index = "A"
    goal_index = "A"

    vertices = ["S", "A", "B", "C", "D", "E", "F", "G"]

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

    weights = [2, 5, 2, 1, 4, 5, 2, 4, 3,
               2, 5, 2, 1, 4, 5, 2, 4, 3]

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
    graph.give_weight(weights)
    graph.give_heuristic(heuristics)

    ucs_path, ucs_cost = u.ucs(graph, start_node, goal_node[0]) 
    a_star_path, a_star_cost = a.a_star(graph, start_node, goal_node)

    print("Expected Path: ['S', 'A', 'D', 'E', 'F', 'G'] \nExpected Cost: 13\n")

    print("UCS")
    print("Path: ", ucs_path, "\nCost: ", ucs_cost, "\n")

    print("A*")
    print("Path: ", a_star_path, "\nCost: ", a_star_cost)
    graph.view()

    print("\nDone")
