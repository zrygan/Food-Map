"""
Uniform Cost Search !
- Exploring a graph blindly based solely on opening up nodes
and their children with the lowest cost until the goal is reached.

Data Structures to use:
    - to_explore queue
    - visited list of some kind

    1. loop while the to_explore queue is not empty
    2.      get the node with the lowest cost (current)
    3.      if the current node is the goal, return the path
    4.      loop through all the neighbors of the current node
    5.          compute the cost of the neighbors of the current node
    6.          if the neighbor is not in visited and its cost is lower than the current neighbor's cost
    7.              add the neighbor to the to_explore queue and update its cost as the current neighbor's cost plus the edge cost

References:
- https://www.educative.io/answers/what-is-uniform-cost-search
"""

def ucs(graph, start, goal):
