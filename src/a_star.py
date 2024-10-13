# work in progress ! ! ! also to be tested

from imports import *

def trace_path():
    # should use parent_list

def compute_g():
    # should use g_values list
    # you can apply dynamic programming!!

def a_star(graph, start_index, goals):
    #ill rewrite this later xp
    """Executes the A* algorithm and returns an optimal path from start node to goal node.

        Args:
            graph: given graph
            start_index: starting index
            goals: list of goal nodes (cus there might be multiple goals)
        Raises:

    """
    #make sure the parameters are valid
    if len(graph.vertices) < 1 or start_index not in graph.vertices or any(index not in graph.vertices for index in goals):
        return None

    #A* algorithm pseudocode

    #1. Initialize:
    #    closed_list (for visited nodes, using list or set)
    #    open_list (for candidate nodes, using priority queue w/ heapq)
    #    g_values (keeps track of the total cost of a node from starting node)
    #    parent_list (to find path easily, using dictionary(?))"""

    closed_list = set()
    open_list = IndexedPriorityQueue()
    g_values = {start_index: 0}
    parent_list = {}

    #2. Add start node in open_list
    open_list.push(start_index, graph.heuristic[start_index])
    #3. While open_list is not empty:
    while len(open_list) > 0:
        #4. Select node w/ lowest f value from open_list. Set this as current node
        #   (Recall f = g + h, where g = sum of actual weight from start to current node & h = heuristic value)
        current = open_list.pop()[0][0]
        print(current)
        #5. If current node is goal node:
        if current in goals:
            found_goal = goals[goals.index(current)]
        #6. Stop algorithm, trace_path() and return the path and total cost
            return trace_path(), g_values[current]
        #7. Else:
        else:
            #8. Add current node to closed_list
            closed_list.add(current)
            #9. For each neighbor of the current node:
            for neighbor in graph.get_neighbors(current):
                #10. If the neighbor is in closed_list, skip
                if neighbor in closed_list:
                    continue
                #11. If the neighbor is not in open_list:
                if neighbor not in open_list:
                    #12. Compute its g value (using compute_g())
                    g = compute_g()
                    #13. Get its h value
                    h = graph.heuristic[neighbor]
                    f = g + h
                    #14. Add it to open_list with f = g + h and set the parent of the neighbor to the current node.
                    open_list.push(neighbor, f)
                    parent_list[neighbor] = current
                    g_values[neighbor] = g
                #15. If the neighbor is already in open_list:
                else:
                    g = compute_g()
                    #16. If the new g value is lower than the current g value:
                    if g < g_values[neighbor]:
                        # 17. Update the neighbor’s g and f values and update its parent to the current node.
                        g_values[neighbor] = g
                        h = graph.heuristic[neighbor]
                        f = g + h

                        open_list.update(neighbor, f)
                        parent_list[neighbor] = current
    #18. If the open list is empty: The goal is unreachable; return failure.
    return None
    #Ref: https://www.geeksforgeeks.org/a-search-algorithm-in-python/
