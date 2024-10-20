from imports import IndexedPriorityQueue

"""
    Performs Uniform Cost Search to find the shortest path from the start vertex to the goal vertex.

    Args:
        graph (Graph): A graph object containing the vertices and edges.
        start (String): The starting vertex.
        goal (String): The goal vertex.
"""

def ucs(graph, start, goal):
    # initialization
    pq = IndexedPriorityQueue()
    pq.push(start, 0) #start with 0 cost
    
    predecessors = {start: None} # stores the predecessors for each vertex into a dictionary, path will be made later on through backtracking
    # each node's value is their predecessor. start has no predecessor so it's none.

    costs = {start: 0} # costs of traversals, start is 0 since it doesn't cost anything
    # loop while there are still open vertices
    
    while pq:
        current_vertex, current_cost = pq.pop() # get the vertex with the lowest cost

        # check if the goal vertex has been reached
        if current_vertex == goal:
            path = []
            
            # backtrack from the goal vertex to the start and use as path
            while current_vertex is not None:
                path.insert(0, current_vertex) # insert at the beginning to build the path backwards
                current_vertex = predecessors[current_vertex]
    
            # return the path and its cost of traversal
            return path, current_cost

        # traverse the neighbors of the current vertex to check all options
        for neighbor in graph.get_neighbors(current_vertex):
            edge_weight = graph.weights.get((current_vertex, neighbor)) 
            if edge_weight is None: 
                continue # skip this neighbor since it has no weight
            new_cost = current_cost + edge_weight
            
            # check if the current path costs lower than the previous path
            if neighbor not in costs or new_cost < costs[neighbor]: #either a completely new neighbor OR a lower cost going to a neighbor
                costs[neighbor] = new_cost  # update cost for the neighbor
                predecessors[neighbor] = current_vertex  # update predecessor for backtracking

                # if neighbor is already in the priority queue, update its priority
                if neighbor in pq:
                    pq.update(neighbor, new_cost)
                else:
                    pq.push(neighbor, new_cost)

    return None, None # Nn path found; goal does not exist / is not reachable

# Reference: https://www.educative.io/answers/what-is-uniform-cost-search