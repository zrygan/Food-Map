# main
# contains the main function for the project
    
from imports import *
from graph import *

if __name__ == "__main__":
    n_vertices = 3
    n_edges = 2
    
    nodes = ["Pericos", "Agno", "Starbs"]
    edges = [("Pericos", "Agno"), ("Starbs", "Agno")]
    weights = [10, 3]
    heuristics = {"Pericos": 10, "Agno": 9, "Starbs": 18} 
    
    
    sample = Graph(n_edges, n_vertices)
    sample.make(nodes, edges)
    sample.give_weight(weights)
    sample.give_heuristic(heuristics)
    sample.view()
    
    print("Done")