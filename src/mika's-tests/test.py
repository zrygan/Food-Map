# main
# contains the main function for the project

from imports import *
from graph import *
import a_star as a
import ucs as u

if __name__ == "__main__":
    vertices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
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

    weights = [6, 3, 3, 2, 1, 5, 8, 5, 5, 1, 7, 3, 2, 3,
               6, 3, 3, 2, 1, 5, 8, 5, 5, 1, 7, 3, 2, 3]

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
    graph.give_weight(weights)
    graph.give_heuristic(heuristics)

    ucs_path, ucs_cost = u.ucs(graph, start_node, goal_node[0]) 
    a_star_path, a_star_cost = a.a_star(graph, start_node, goal_node)
    
    print("Expected Path: ['A', 'F', 'G', 'I', 'J']\nExpected Cost: 10\n")
    
    print("UCS")
    print("Path: ", ucs_path, "\nCost: ", ucs_cost, "\n")

    print("A*")
    print("Path: ", a_star_path, "\nCost: ", a_star_cost)

    graph.view()

    print("\nDone!")
