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
        for vertex, heuristic in heuristics:
            if vertex in self.vertices:
                self.heuristic[vertex] = heuristic
            else:
                raise ValueError(f"The vertex {vertex} NOT FOUND in the Graph.")

    def view(self, path: list[int]=None) -> None:
        """View the plot as a UI.

        Args:
            path (list[int], optional): the list of the algorithm traversal. Defaults to None.
        """
        # Create a Tkinter window
        window = tk.Tk()
        window.title("Graph Visualization")

        # Create a frame for the plot
        plot_frame = Frame(window)
        plot_frame.pack(side="left", padx=10, pady=10)

        # Create a figure for the plot
        fig, ax = plt.subplots()

        # Draw the graph
        positions = nx.spring_layout(self.G)

        if path is None:
            node_color = ["black" for node in self.G.nodes]
            edge_color = ["black" for u, v in self.G.edges]
        else:
            node_color = ["red" if node in path else "black" for node in self.G.nodes]
            edge_color = ["darkred" if (u in path and v in path) else "black" for u, v in self.G.edges]


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
            offset = 0.15
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

        # TODO: Add input for start index
        # TODO: Add input for end index
        # TODO: Add input for type of Algorithm
        
        # Add the plot as a Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        # Add the tool bar        
        toolbar_frame = Frame(window)
        toolbar_frame.pack(side="top", fill="x")
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
        toolbar.update()
        canvas._tkcanvas.pack(side="top", fill="both", expand=True)

        # Add a sidebar for the legends
        legend_frame = Frame(window)
        legend_frame.pack(side="right", padx=10, pady=10)
        for node in self.G.nodes:
            # TODO: add the node number before each legend
            label_text = f"{node}: {self.vertices.get(node)}"
            label = Label(legend_frame, text=label_text, fg="black") 
            label.pack(anchor="w")

        window.mainloop()
    
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
        for edge in edges_to_add:
            if edge not in self.edges and edge[::-1] not in self.edges:
                self.G.add_edge(edge[0], edge[1])
                self.edges.append(edge)
                
    def remove_edge(self, edge_to_remove: tuple[int,int]) -> None:
        """algorithm for edge removal.
        Consideration:
            We want to maintain graph connectivity such that 
            removing some edge v from g does not result in two
            separate graphs g1 and g2. edge(g[v]) => g1, g2. 
        
        This is done through a dfs algorithm implementation.

        Args:
            edge_to_remove (tuple[int,int]): the edge to remove from the graph
        """
        def verification() -> bool:
            """verifies if the graph is still a connected graph.
            Uses dfs from `dfs.py`.

            Returns:
                bool: returns true if the graph is a connected graph, false otherwise
            """
            visited = set()
            
            s = next(iter(self.vertices))
            dfs(self,s,visited)
            
            return len(visited) == len(self.vertices)
        
        if edge_to_remove in self.edges or (edge_to_remove[1],edge_to_remove[0]) in self.edges:
            self.edges.remove(edge_to_remove)
            self.G.remove_edge(edge_to_remove[0], edge_to_remove[1])
            
            if not verification():
                self.edges.append(edge_to_remove)
                self.G.add_edge(edge_to_remove[0], edge_to_remove[1])

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
