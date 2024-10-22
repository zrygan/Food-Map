# graph
# contains all the files to create and view the graph

from imports import *

class Graph:
    """A graph object
    """

    def __init__(self, num_edges: int, num_vertex: int) -> None:
        """Initialize the Graph object using nx.

        Args:
            num_edges (int): number of edges the graph has
            num_vertex (int): number of vertices the graph has
        """
        self.G = nx.Graph()
        self.num_edges = num_edges
        self.num_vertex = num_vertex
        self.edges = []
        self.vertices = []
        self.weights = {}
        self.heuristic = {}

    def make(self, vertices: list[int], edges: list[tuple[int, int]]) -> None:
        """Creates the Graph object by adding the vertices and edges to it.

        Args:
            vertices (list[int]): the array of vertices in G
            edges (list[tuple[int, int]]): the array of ordered pairs of vertices
        """
        self.G.add_nodes_from(vertices)
        self.G.add_edges_from(edges)

        self.vertices = vertices
        self.edges = edges

    def give_weight(self, weights: list[float]) -> None:
        """Gives the weight of each edge in the graph.

        Args:
            weights (list[float]): an array of floats that is the weight of each edge.
        """
        if len(weights) > 0 and len(weights) != len(self.edges):
            raise ValueError("Number of weights MUST BE equal to the number of edges.")

        for edge, weight in zip(self.edges, weights):
            self.G[edge[0]][edge[1]]["weight"] = weight
            self.weights[edge] = weight

    def give_heuristic(self, heuristics: dict[int, float]) -> None:
        """Gives the heuristics value of each vertex in the graph.

        Args:
            heuristics (dict[int(value, base), float]): a dictionary of vertices and their heuristic values.
        """
        for vertex, heuristic in heuristics.items():
            if vertex in self.vertices:
                self.heuristic[vertex] = heuristic

    def view(self, path: list[int]=None, start_node: int=None, end_node: int=None) -> None:
        """View the plot as a UI.

        Args:
            path (list[int], optional): the list of the algorithm traversal. Defaults to None.
            start_node (int, optional): the start node. Defaults to None.
            end_node (int, optional): the end node. Defaults to None.
        """
        # Create a figure for the plot
        fig, ax = plt.subplots()

        # Draw the graph
        positions = nx.spring_layout(self.G)

        node_color = []
        for node in self.G.nodes:
            if node == start_node:
                node_color.append("green")
            elif node == end_node:
                node_color.append("darkred")
            elif path and node in path:
                node_color.append("red")
            else:
                node_color.append("grey")

        edge_color = ["darkred" if path and (u in path and v in path) else "black" for u, v in self.G.edges]

        nx.draw(
            self.G,
            positions,
            with_labels=True,
            node_color=node_color,
            node_size=700,
            font_size=8,
            font_color="white",
            edge_color=edge_color,
            ax=ax,
        )
        plt.title("Graph of Food Map")

        # Show heuristic values beside each vertex
        if self.heuristic:
            heuristic_labels = {vertex: self.heuristic[vertex] for vertex in self.heuristic}
            offset = 0.05
            heuristic_label_positions = {
                vertex: (pos[0], pos[1] + offset) for vertex, pos in positions.items()
            }
            nx.draw_networkx_labels(
                self.G,
                heuristic_label_positions,
                labels=heuristic_labels,
                font_color="blue",
                ax=ax,
            )

        # Show weights of each edge beside it
        if self.weights:
            edge_labels = nx.get_edge_attributes(self.G, "weight")
            nx.draw_networkx_edge_labels(self.G, positions, edge_labels=edge_labels, ax=ax)

        plt.show()
    
    def get_neighbors(self, vertex: int) -> None:
        """Returns an iterator containing the neighbors of a given vertex.

            Args:
                vertex (str): A vertex in the graph

            Raises:
                ValueError: If a vertex is not found in the graph.
        """
        if vertex in self.vertices:
            return self.G.neighbors(vertex)
        else:
            raise ValueError(f"The vertex {vertex} NOT FOUND in the Graph.")
    
    def remove_vertex(self, vertex_to_remove: int) -> None:
        """removes a vertex from the graph and adjusts all graph logistics to fit the node removal.

        Args:
            vertex_to_remove (int): the node to remove
        """
        
        def return_first_adjacent() -> int:
            """the first adjacent node to the node to be removed

            Returns:
                int: the first adjacent node, (-1) if it does not exist
            """
            for edge in self.edges:
                if vertex_to_remove in edge:
                    return edge[0] if edge[0] != vertex_to_remove else edge[1]
            return -1

        adjacent = return_first_adjacent()
        edges_copy = []

        if adjacent != -1:
            for edge in self.edges:
                if vertex_to_remove in edge:
                    new_edge = (adjacent, edge[1] if edge[0] == vertex_to_remove else edge[0])
                    if new_edge[0] != new_edge[1]:                    
                        edges_copy.append(new_edge)
                else:
                    edges_copy.append(edge)

            self.edges = edges_copy
            del self.vertices[vertex_to_remove]

            self.G.clear()
            self.G.add_edges_from(self.edges)
            self.G.add_nodes_from(self.vertices)
            
    def add_vertex(self, vertex_to_add: int, edges_to_add: tuple[int,int], new_vertex_name: str=None) -> None:
        """adds a vertex to the graph

        Args:
            vertex_to_add (int): the vertex to add
            edges_to_add (tuple[int,int]): an edge to add to maintain the connectivity of the graph
            new_vertex_name (str, optional): the name or title of the vertex. Defaults to None.
        """
        new_vertex_checker = any(vertex_to_add in edge for edge in edges_to_add)
        not_dupe_checker = any(vertex_to_add != vertex for vertex in self.vertices.keys())
        

        if new_vertex_checker and not_dupe_checker:
            if new_vertex_name is None:
                new_vertex_name = "new_vertex_" + str(vertex_to_add)
            
            self.G.add_node(vertex_to_add)
            self.vertices[vertex_to_add] = new_vertex_name
            self.G.add_edges_from(edges_to_add)
            self.edges.append(edges_to_add)
            
    def add_edge(self, edges_to_add: tuple[int,int]) -> None:
        """adds an edge

        Args:
            edges_to_add (tuple[int,int]): the edge to add
        """
        for edge in edges_to_add:
            if edge not in self.edges and (edge[1], edge[0]) not in self.edges:
                self.G.add_edge(edge[0], edge[1])
                self.edges.append(edge)
                
    def remove_edge(self, edge_to_remove: tuple[int, int]) -> None:
        """Algorithm for edge removal.
        Consideration:
            We want to maintain graph connectivity such that 
            removing some edge v from g does not result in two
            separate graphs g1 and g2. edge(g[v]) => g1, g2. 
        
        This is done through a dfs algorithm implementation.

        Args:
            edge_to_remove (tuple[int, int]): the edge to remove from the graph
        """
        def verification() -> bool:
            """Verifies if the graph is still a connected graph.
            Uses dfs from `dfs.py`.

            Returns:
                bool: Returns true if the graph is a connected graph, false otherwise
            """
            visited = set()
            
            s = next(iter(self.vertices))
            dfs(self, s, visited)
            
            return len(visited) == len(self.vertices)
        
        if edge_to_remove in self.edges:
            self.edges.remove((edge_to_remove[0], edge_to_remove[1]))
            self.edges.remove((edge_to_remove[1], edge_to_remove[0]))
                
            self.G.remove_edge(edge_to_remove[0], edge_to_remove[1])
            # remove mirror
            # self.G.remove_edge(edge_to_remove[1], edge_to_remove[0])
            
            if not verification():
                self.edges.append(edge_to_remove)
                self.G.add_edge(edge_to_remove[0], edge_to_remove[1])

    def add_change_heuristic(self, vertex: int, heuristic_to_add: float) -> None:
        """Adds or changes a heuristic

        Args:
            vertex (int): the vertex to change or add a heuristic value
            heuristic_to_add (float): the heuristic value
        """
        if vertex in self.vertices:
            self.heuristic[vertex] = heuristic_to_add
            
    def add_change_edge(self, edge: tuple[int, int], weight: float) -> None:
        """Adds or changes a weight for an edge

        Args:
            edge (tuple[int, int]): the edge
            weight (float): the weight of this edge
        """
        if edge in self.edges or (edge[1], edge[0]) in self.edges:
            self.G[edge[0]][edge[1]]["weight"] = weight
            self.weights[edge] = weight    

def dfs(graph: Graph, vertex: int, visited: set[int], goal_node: int = None) -> bool:
    """A depth-first search implementation (DFS).
    Has an optional feature to use for searching a goal node.

    Args:
        graph (Graph): The graph to traverse.
        vertex (int): The current vertex to visit.
        visited (set[int]): A set to track visited vertices.
        goal_node (int, optional): The target node to search for. Defaults to None.

    Returns:
        bool: True if the goal node is found, False otherwise.
    """
    visited.add(vertex)

    if vertex == goal_node:
        return True
    
    for neighbor in sorted(graph.get_neighbors(vertex)):
        if neighbor not in visited:
            if dfs(graph, neighbor, visited, goal_node):
                return True

    return False
