import heapq

#i still don't know the exact algorithm for this function, but it will use parent_list
def trace_path(start, parent_list):
    #insert code

def compute_g(start, end):
    #insert code

def a_star(graph, start, goal):
    """
    A* algorithm pseudocode

    1. Initialize:
        closed_list (for visited nodes, using list or set)
        open_list (for candidate nodes, using priority queue w/ heapq)
        parent_list (to find path easily, using dictionary(?))
    2. Add start node in open_list
    3. While open_list is not empty:
    4.      Select node w/ lowest f value from open_list. Set this as current node
            (Recall f = g + h, where g = sum of actual weight from start to current node & h = heuristic value)
    5.      If current node is goal node:
    6.          Stop algorithm, trace_path() and return it
    7.      Else:
    8.          Add current node to closed_list
    9.          For each neighbor of the current node:
    10.             If the neighbor is in closed_list, skip
    11.             If the neighbor is not in open_list:
    12.                 Compute its g value (using compute_g())
    13.                 Get its h value
    14.                 Add it to open_list with f = g + h and set the parent of the neighbor to the current node.
    15.             If the neighbor is already in open_list:
    16.                 If the new g value is lower than the current g value:
    17.                     Update the neighbor’s g and f values and update its parent to the current node.
    18. If the open list is empty:
    19.     The goal is unreachable; return failure.

    Ref: https://www.geeksforgeeks.org/a-search-algorithm-in-python/
    """
    closed_list = []
    open_list = []
    parent_list = []
    #insert code
