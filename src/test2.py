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

    vertices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]

    edges = [("A", "B"), ("A", "C"),
             ("B", "D"),
             ("C", "D"), ("C", "F"), ("C", "L"),
             ("D", "E"),
             ("E", "G"),
             ("F", "J"), ("F", "K"),
             ("G", "H"),
             ("H", "I"),
             ("I", "J"),
             ("J", "K"),
             ("K", "M"),
             ("L", "M"),

             ("B", "A"), ("C", "A"),
             ("D", "B"),
             ("D", "C"), ("F", "C"), ("L", "C"),
             ("E", "D"),
             ("G", "E"),
             ("J", "F"), ("K", "F"),
             ("H", "G"),
             ("I", "H"),
             ("J", "I"),
             ("K", "J"),
             ("M", "K"),
             ("M", "L")
             ]

    weights = [15, 35, 15, 32, 15, 80, 10, 10, 95, 90, 10, 15, 20, 25, 15, 95,
               15, 35, 15, 32, 15, 80, 10, 10, 95, 90, 10, 15, 20, 25, 15, 95]

    heuristics = {
        "A": 90,
        "B": 85,
        "C": 50,
        "D": 65,
        "E": 100,
        "F": 55,
        "G": 95,
        "H": 75,
        "I": 55,
        "J": 45,
        "K": 30,
        "L": 35,
        "M": 0
    }

    start_node = "A"
    goal_node = ["M"]

    graph = Graph(len(edges), len(vertices))
    graph.make(vertices, edges)
    graph.give_weight(weights)
    graph.give_heuristic(heuristics)

    a_star_path, a_star_cost = a.a_star(graph, start_node, goal_node)
    print("Expected Path: ['A', 'B', 'D', 'E', 'G', 'H', 'I', 'J', 'K', 'M']\nExpected Cost: 135\n")

    print("A*")
    print("Path: ", a_star_path, "\nCost: ", a_star_cost)
    graph.view()


    print("Done")
