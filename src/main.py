# main
# contains the main function for the project

from graph import *
from ucs import *
from a_star import *
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
            "make": {
                "function": self.make,
                "description": "Initialize the graph using predefined rules. Input format: make",
                "success_message": "Graph initialized using rules."
            },
            "exit": {
                "function": lambda: False,
                "description": "Exit the program. Input format: exit",
                "success_message": "Exiting program."
            },
            "set start": {
                "function": self.set_start_index,
                "description": "Set the start index to the specified number. Input format: set start <number>",
                "success_message": "Start index set."
            },
            "set goal": {
                "function": self.set_goal_index,
                "description": "Set the goal index to the specified number. Input format: set goal <number>",
                "success_message": "Goal index set."
            },
            "view": {
                "function": self.view_graph,
                "description": "View the current graph. Input format: view",
                "success_message": "Graph viewed."
            },
            "view result": {
                "function": self.view_result,
                "description": "View the graph with start, end vertices, and the result of the algorithm as the path. Input format: view result <algorithm>",
                "success_message": "Graph viewed with start, end vertices, and algorithm result."
            },
            "show start": {
                "function": self.show_start,
                "description": "Show the current start index. Input format: show start",
                "success_message": "Start index shown."
            },
            "show goal": {
                "function": self.show_goal,
                "description": "Show the current goal index. Input format: show goal",
                "success_message": "Goal index shown."
            },
            "add vertex": {
                "function": self.add_vertex,
                "description": "Add a vertex to the graph. Input format: add vertex <number>",
                "success_message": "Vertex added."
            },
            "del vertex": {
                "function": self.del_vertex,
                "description": "Delete a vertex from the graph. Input format: del vertex <number>",
                "success_message": "Vertex deleted."
            },
            "add edge": {
                "function": self.add_edge,
                "description": "Add an edge to the graph. Input format: add edge <u> <v>",
                "success_message": "Edge added."
            },
            "del edge": {
                "function": self.del_edge,
                "description": "Delete an edge from the graph. Input format: del edge <u> <v>",
                "success_message": "Edge deleted."
            }
        }

    def make(self) -> None:
        """initializes the graph using the rules established
        """
        vertices = {
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
            
        heuristics = {
            1: 3.9,
            2: 4.2,
            3: 4.0,
            4: 4.5,
            5: 4.2,
            6: 3.0,
            7: 3.4,
            8: 4.2,
            9: 3.8,
            10: 4.0,
            11: 4.1,
            12: 3.7,
            13: 4.1,
            14: 4.1,
            15: 2.0,
            16: 2.5,
            17: 3.0,
            18: 4.5,
            19: 3.0,
            20: 2.9,
            21: 2.5
        }

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
                self.add_edge(vertex, v)
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
                self.graph.remove_vertex(vertex)
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
            self.graph.view(start_node=self.start_index, end_node=self.goal_index)

    def view_result(self, algorithm:str):
        """View the graph with all decorations

        Args:
            algorithm (str): the algorithm to run
        """
        if not self.graph or not self.graph.vertices:
            print("Graph is not initialized.")
        else:
            algorithm = algorithm.lower()
            if algorithm == "dfs":
                visited = set()
                dfs(self.graph, self.start_index, visited, self.goal_index)
                visited = list(visited)
                
                # output
                self.print_vertices(visited)
                print("Path:", visited)
                self.graph.view(visited, self.start_index, self.goal_index)
            
            elif algorithm == "ucs":
                path, cost = ucs(self.graph, self.start_index, self.goal_index)
                
                #output
                self.print_vertices(path)
                print("Path:", path)
                print("Path:", cost)
                self.graph.view(path, self.start_index, self.goal_index)
            elif algorithm == "a*":
                path, cost = a_star(self.graph, self.start_index, self.goal_index)
                
                #output
                self.print_vertices(path)
                print("Path:", path)
                print("Path:", cost)
                self.graph.view(path, self.start_index, self.goal_index) 
            else:
                print("Invalid comamnd. Unknown algorithm", algorithm)

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
            elif choice.startswith("view result "):
                try:
                    algorithm = choice.split()[2]
                    self.commands["view result"]["function"](algorithm)
                    print(self.commands["view result"]["success_message"])
                except (IndexError, ValueError):
                    print("Invalid command. Usage: view result <algorithm>")
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
                    print(f"{Fore.LIGHTYELLOW_EX}{command}{Fore.WHITE} : {details['description']}")
            else:
                print("Invalid command. Please type ? for commands.")  

if __name__ == "__main__":
    graph_manager = GraphManager()
    graph_manager.update_loop()