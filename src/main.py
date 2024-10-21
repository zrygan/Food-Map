# main
# contains the main function for the project

from graph import Graph
from imports import *
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class GraphManager:
    """The main CLI
    """
    def __init__(self):
        """Initializes the objects and commands in the CLI
        """
        self.graph = None
        self.start_index = -1
        self.goal_index = -1
        self.commands = {
            "make rules": {
                "function": self.using_rules,
                "description": "Initialize the graph using predefined rules.",
                "success_message": "Graph initialized using rules."
            },
            "exit": {
                "function": lambda: False,
                "description": "Exit the program.",
                "success_message": "Exiting program."
            },
            "set start": {
                "function": self.set_start_index,
                "description": "Set the start index to the specified number.",
                "success_message": "Start index set."
            },
            "set goal": {
                "function": self.set_goal_index,
                "description": "Set the goal index to the specified number.",
                "success_message": "Goal index set."
            },
            "view": {
                "function": self.view_graph,
                "description": "View the current graph.",
                "success_message": "Graph viewed."
            },
            "view se": {
                "function": self.view_start_end,
                "description": "View the graph with start and end vertices highlighted.",
                "success_message": "Graph viewed with start and end vertices highlighted."
            },
            "view res": {
                "function": self.view_result,
                "description": "View the graph with the result of the algorithm as the path.",
                "success_message": "Graph viewed with algorithm result."
            },
            "view all": {
                "function": self.view_all,
                "description": "View the graph with start, end vertices, and the result of the algorithm as the path.",
                "success_message": "Graph viewed with start, end vertices, and algorithm result."
            },
            "show start": {
                "function": self.show_start,
                "description": "Show the current start index.",
                "success_message": "Start index shown."
            },
            "show goal": {
                "function": self.show_goal,
                "description": "Show the current goal index.",
                "success_message": "Goal index shown."
            },
            "add vertex": {
                "function": self.add_vertex,
                "description": "Add a vertex to the graph.",
                "success_message": "Vertex added."
            },
            "del vertex": {
                "function": self.del_vertex,
                "description": "Delete a vertex from the graph.",
                "success_message": "Vertex deleted."
            },
            "add edge": {
                "function": self.add_edge,
                "description": "Add an edge to the graph.",
                "success_message": "Edge added."
            },
            "del edge": {
                "function": self.del_edge,
                "description": "Delete an edge from the graph.",
                "success_message": "Edge deleted."
            }
        }
    
    def initialize_vertices(self) -> dict[int, str]:
        """Initializes the vertices

        Returns:
            dict[int, str]: the vertices (a dictionary)
        """
        return {
            1: "University Mall",
            2: "Mcdonald's",
            3: "Perico's",
            4: "Bloemen Hall",
            5: "W.H Taft Residence",
            6: "EGI Taft",
            7: "Castro Street",
            8: "Agno Food Court",
            9: "One Archers'",
            10: "La Casita",
            11: "Green Mall",
            12: "Green Court",
            13: "Sherwood",
            14: "Jolibee",
            15: "Dagonoy St.",
            16: "Burgundy",
            17: "Estrada St.",
            18: "D' Student's Place",
            19: "Leon Guinto St.",
            20: "P. Ocampo St.",
            21: "Fidel A. Reyes St.",
        } 

    def using_rules(self) -> None:
        """initializes the graph using the rules established
        """
        vertices = self.initialize_vertices()
        edges = [
            (21, 10),
            (10, 11),
            (10, 12),
            (8, 12),
            (10, 9),
            (9, 14),
            (14, 13),
            (9, 7),
            (7, 6),
            (6, 5),
            (5, 4),
            (5, 15),
            (15, 19),
            (19, 16),
            (15, 16),
            (16, 17),
            (17, 18),
            (18, 20),
            (20, 1),
            (1, 2),
            (2, 3),
            (3, 1)
        ]
                
        weights = []
        heuristics = []

        self.graph = Graph(len(edges), len(vertices))
        self.graph.make(vertices, edges)
        self.graph.give_weight(weights)
        self.graph.give_heuristic(heuristics)

    def set_start_index(self, index=-1):
        """Sets the start index

        Args:
            index (int, optional): the new start index. Defaults to -1.
        """
        if not self.graph or not self.graph.vertices:
            print("Graph is not initialized. Please initialize the graph first.")
        elif index == -1 or index not in self.graph.vertices:
            print(f"Invalid start index. Vertex {index} does not exist.")
        else:
            self.start_index = index
            print(f"Start index set to {self.start_index}.")

    def set_goal_index(self, index=-1):
        """Sets the goal index

        Args:
            index (int, optional): the new goal index. Defaults to -1.
        """
        if not self.graph or not self.graph.vertices:
            print("Graph is not initialized. Please initialize the graph first.")
        elif index == -1 or index not in self.graph.vertices:
            print(f"Invalid goal index. Vertex {index} does not exist.")
        else:
            self.goal_index = index
            print(f"Goal index set to {self.goal_index}.")

    def show_start(self):
        """Getter for the start index
        """
        if self.start_index == -1:
            print("Start index is not set.")
        else:
            print(f"Start index: {self.start_index} - {self.graph.vertices.get(self.start_index, 'Unknown')}")

    def show_goal(self):
        """Getter for the goal index
        """
        if self.goal_index == -1:
            print("Goal index is not set.")
        else:
            print(f"Goal index: {self.goal_index} - {self.graph.vertices.get(self.goal_index, 'Unknown')}")

    def add_vertex(self, vertex: int):
        """Adds a vertex in the graph

        Args:
            vertex (int): the vertex to add
        """
        if not self.graph:
            print("Graph is not initialized. Please initialize the graph first.")
        else:
            if vertex not in self.graph.vertices:
                name = input("name: ").strip()
                v = int(input("edge: ").strip())
                self.graph.vertices[vertex] = name
                self.graph.G.add_node(vertex)
                self.add_edge(99, v)
                print(f"\nVertex {vertex} with name '{name}' added.")
            else:
                print(f"Vertex {vertex} already exists.")

    def del_vertex(self, vertex: int):
        """Deleted a vertex in the graph

        Args:
            vertex (int): the vertex to delete
        """
        if not self.graph:
            print("Graph is not initialized. Please initialize the graph first.")
        else:
            if vertex in self.graph.vertices:
                del self.graph.vertices[vertex]
                self.graph.G.remove_node(vertex)
                self.graph.edges = [edge for edge in self.graph.edges if vertex not in edge]
                print(f"Vertex {vertex} removed.")
            else:
                print(f"Vertex {vertex} does not exist.")

    def add_edge(self, u: int, v: int):
        """Adds an edge in the graph

        Args:
            u (int): the first component
            v (int): the second component
        """
        if not self.graph:
            print("Graph is not initialized. Please initialize the graph first.")
        else:
            edge = (u, v)
            if edge not in self.graph.edges and (v, u) not in self.graph.edges:
                self.graph.edges.append(edge)
                self.graph.G.add_edge(u, v)
                print(f"Edge {edge} added.")
            else:
                print(f"Edge {edge} already exists.")

    def del_edge(self, u: int, v: int):
        """Deletes an edge in the graph

        Args:
            u (int): the first component
            v (int): the second component
        """
        if not self.graph:
            print("Graph is not initialized. Please initialize the graph first.")
        else:
            edge = (u, v)
            rev = (v, u)
            if edge in self.graph.edges:
                self.graph.edges.remove(edge)
                self.graph.G.remove_edge(u, v)
                print(f"Edge {edge} removed.")
            elif rev in self.graph.edges:
                self.graph.edges.remove(rev)
                self.graph.G.remove_edge(v, u)
                print(f"Edge {rev} removed.")
            else:
                print(f"Edge {edge} does not exist.")

    def print_vertices(self, path:list[int]=None):
        """Prints the vertices and adds color

        Args:
            path (list[int], optional): the path of the algorithm. Defaults to None.
        """
        for index, name in self.graph.vertices.items():
            if index == self.goal_index:
                print(f"{index}\t{Fore.GREEN}{name}")
            elif index == self.start_index:
                print(f"{index}\t{Fore.YELLOW}{name}")
            elif path and index in path:
                print(f"{index}\t{Fore.LIGHTBLACK_EX}{name}")
            else:
                print(f"{index}\t{name}")

    def view_graph(self):
        """View the graph without additional decoration
        """
        if not self.graph or not self.graph.vertices:
            print("Graph is not initialized.")
        else:
            self.print_vertices()
            self.graph.view()

    def view_start_end(self):
        """View the graph where the start and goal are highlighted
        """
        if not self.graph or not self.graph.vertices:
            print("Graph is not initialized.")
        else:
            self.print_vertices()
            self.graph.view(start_node=self.start_index, end_node=self.goal_index)

    def view_result(self, algorithm:str):
        """Vuew the graph where the best path of the algorithm is highlighted

        Args:
            algorithm (str): the algorithm to run
        """
        if not self.graph or not self.graph.vertices:
            print("Graph is not initialized.")
        else:
            path = self.run_algorithm(algorithm)
            self.print_vertices(path=path)
            self.graph.view(path=path)

    def view_all(self, algorithm:str):
        """View the graph with all decorations

        Args:
            algorithm (str): the algorithm to run
        """
        if not self.graph or not self.graph.vertices:
            print("Graph is not initialized.")
        else:
            path = self.run_algorithm(algorithm)
            self.print_vertices(path=path)
            self.graph.view(path=path, start_node=self.start_index, end_node=self.goal_index)

    def run_algorithm(self, algorithm:str) -> list[int]:
        """Runs the algorithm

        Args:
            algorithm (str): the algorithm to run

        Returns:
            list[int]: the list of vertices (the best path) 
        """
        if algorithm.lower() == "ucs":
            pass # TODO: ADD THE ALGORITHM HERE
        elif algorithm.lower() == "a*":
            pass # TODO: ADD THE ALGORITHM HERE
        elif algorithm.lower() == "dfs":
            pass # TODO: ADD THE ALGORITHM HERE
        else:
            print(f"Unknown algorithm: {algorithm}")
            return []

    def update_loop(self) -> None:
        """The main program loop
        """
        while True: 
            print()
            print(">>> ", end="") 
            choice = input().strip().lower()
            print()
            
            if choice in self.commands:
                result = self.commands[choice]["function"]()
                if result is False:
                    break
                else:
                    print(self.commands[choice]["success_message"])
            elif choice.startswith("set start "):
                try:
                    index = int(choice.split()[2])
                    self.commands["set start"]["function"](index)
                    print(self.commands["set start"]["success_message"])
                except (IndexError, ValueError):
                    self.commands["set start"]["function"]()
                    print("Invalid command. Usage: set start <number>")
            elif choice.startswith("set goal "):
                try:
                    index = int(choice.split()[2])
                    self.commands["set goal"]["function"](index)
                    print(self.commands["set goal"]["success_message"])
                except (IndexError, ValueError):
                    self.commands["set goal"]["function"]()
                    print("Invalid command. Usage: set goal <number>")
            elif choice.startswith("view res "):
                try:
                    algorithm = choice.split()[2]
                    self.commands["view res"]["function"](algorithm)
                    print(self.commands["view res"]["success_message"])
                except (IndexError, ValueError):
                    print("Invalid command. Usage: view res <algorithm>")
            elif choice.startswith("view all "):
                try:
                    algorithm = choice.split()[2]
                    self.commands["view all"]["function"](algorithm)
                    print(self.commands["view all"]["success_message"])
                except (IndexError, ValueError):
                    print("Invalid command. Usage: view all <algorithm>")
            elif choice.startswith("add vertex "):
                try:
                    vertex = int(choice.split()[2])
                    self.commands["add vertex"]["function"](vertex)
                    print(self.commands["add vertex"]["success_message"])
                except (IndexError, ValueError):
                    print("Invalid command. Usage: add vertex <number>")
            elif choice.startswith("del vertex "):
                try:
                    vertex = int(choice.split()[2])
                    self.commands["del vertex"]["function"](vertex)
                    print(self.commands["del vertex"]["success_message"])
                except (IndexError, ValueError):
                    print("Invalid command. Usage: del vertex <number>")
            elif choice.startswith("add edge "):
                try:
                    u, v = map(int, choice.split()[2:4])
                    self.commands["add edge"]["function"](u, v)
                    print(self.commands["add edge"]["success_message"])
                except (IndexError, ValueError):
                    print("Invalid command. Usage: add edge <u> <v>")
            elif choice.startswith("del edge "):
                try:
                    u, v = map(int, choice.split()[2:4])
                    self.commands["del edge"]["function"](u, v)
                    print(self.commands["del edge"]["success_message"])
                except (IndexError, ValueError):
                    print("Invalid command. Usage: del edge <u> <v>")
            elif choice == "?":
                print("Available commands:")
                for command, details in self.commands.items():
                    print(f"{Fore.LIGHTYELLOW_EX}{command}: {details['description']}")
            else:
                print("Invalid command. Please type ? for commands.")  

if __name__ == "__main__":
    graph_manager = GraphManager()
    graph_manager.update_loop()