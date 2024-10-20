# graph
# contains all the files to create and view the graph

from imports import *

class Graph:
    vertices = None

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

        Raises:
            ValueError: If the number of weights does not match the number of edges.
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

        Raises:
            ValueError: If a vertex is not found in the graph.
        """
        for vertex, heuristic in heuristics.items():
            if vertex in self.vertices:
                self.heuristic[vertex] = heuristic
            else:
                raise ValueError(f"The vertex {vertex} NOT FOUND in the Graph.")

    def view(self) -> None:
        """View the plot as a UI."""
        positions = nx.spring_layout(self.G)
        nx.draw(
            self.G,
            positions,
            with_labels=True,
            node_color="black",
            node_size=700,
            font_size=8,
            font_color="white",
            edge_color="black",
        )
        plt.title("Graph of Food Map")

        # Show heuristic values beside each vertex
        if self.heuristic:
            heuristic_labels = {vertex: self.heuristic[vertex] for vertex in self.heuristic}
            offset = 0.15
            heuristic_label_positions = {
                vertex: (pos[0], pos[1] + offset) for vertex, pos in positions.items()
            }
            nx.draw_networkx_labels(
                self.G,
                heuristic_label_positions,
                labels=heuristic_labels,
                font_color="blue",
            )

        # Show weights of each edge beside it
        if self.weights:
            edge_labels = nx.get_edge_attributes(self.G, "weight")
            nx.draw_networkx_edge_labels(self.G, positions, edge_labels=edge_labels)

        plt.show()
    
    def get_neighbors(self, vertex: str):
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