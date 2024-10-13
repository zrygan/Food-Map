from imports import IndexedPriorityQueue

"""
    Performs Uniform Cost Search to find the shortest path from the start vertex to the goal vertex.

    Args:
        graph (Graph): A graph object containing the vertices and edges.
        start (String): The starting vertex.
        goal (String): The goal vertex.
"""

# FIXME: not actually sure if this works \(T-T)/ idk python pls -emmman

def ucs(graph, start, goal):
    # initialization
    open_vertices = [] # list of vertices open / to traverse.
    path = [] # path that will contain the least costly traversal to the goal vertex.
    costs = 0 # costs of traversals 

    # loop while there are still open vertices
    while open_vertices:
        
        # get the vertex with the lowest cost

        # check if the goal vertex has been reached

            # backtrack from the goal vertex to the start and use as path

            # return the path and its cost of traversal

        # traverse the neighbors of the current vertex

            # check if the current path costs lower than the previous path

    return None # No path found; goal does not exist / is not reachable

# Reference: https://www.educative.io/answers/what-is-uniform-cost-search