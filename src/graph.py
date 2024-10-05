# graph
# contains all the files to create and view the graph

from imports import *

class Graph:
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

    def make(self, nodes: list[str], edges: list[tuple[str, str]]):
        """Creates the Graph object by adding the nodes and edges to it.

        Args:
            nodes (list[str]): the array of nodes in G
            edges (list[tuple[str, str]]): the array of ordered pairs of nodes
        """
        self.G.add_nodes_from(nodes)
        self.G.add_edges_from(edges)
        
        self.vertices = nodes
        self.edges = edges

    def give_weight(self, weights: list[float]):
        """Gives the weight of each edge in the graph.

        Args:
            weights (list[float]): an array of floats that is the weight of each edge.

        Raises:
            ValueError: If the number of weights does not match the number of edges.
        """
        if len(weights) > 0 and len(weights) != len(self.edges):
            raise ValueError("Number of weights MUST BE equal to the number of edges.")
        
        for edge, weight in zip(self.edges, weights):
            self.G[edge[0]][edge[1]]['weight'] = weight
            self.weights[edge] = weight

    def give_heuristic(self, heuristics: dict[str, float]):
        """Gives the heuristics value of each vertex in the graph.

        Args:
            heuristics (dict[str, float]): a dictionary of vertices and their heuristic values.

        Raises:
            ValueError: If a vertex is not found in the graph.
        """
        for vertex, heuristic in heuristics:
            if vertex in self.vertices:
                self.heuristic[vertex] = heuristic
            else:
                raise ValueError(f"The vertex {vertex} NOT FOUND in the Graph.")

    def view(self):
        """View the plot as a UI."""
        positions = nx.spring_layout(self.G)
        nx.draw(self.G, positions, with_labels=True, node_color='black', 
                node_size=700, font_size=8, font_color='white', edge_color='black')
        plt.title("Graph of Food Map")

        # Show heuristic values beside each node
        if self.heuristic:
            heuristic_labels = {node: self.heuristic[node] for node in self.heuristic}
            offset = 0.15
            heuristic_label_positions = {node: (pos[0], pos[1] + offset) for node, pos in positions.items()}
            nx.draw_networkx_labels(self.G, heuristic_label_positions, labels=heuristic_labels, font_color='blue')

        # Show weights of each edge beside it
        if self.weights:
            edge_labels = nx.get_edge_attributes(self.G, 'weight')
            nx.draw_networkx_edge_labels(self.G, positions, edge_labels=edge_labels)

        plt.show()