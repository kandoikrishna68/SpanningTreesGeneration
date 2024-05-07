from tkinter import Canvas
from elements import Node, Edge
name_of_nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


class Spanning_Tree_GUI(Canvas):
    def __init__(self, tree, canvas, G):
        super().__init__()
        self.no_of_nodes = len(tree.nodes())
        self.canvas = canvas
        self.Nodes_list = []
        self.x = 45
        self.y = 80
        for creation in range(self.no_of_nodes):
            self.x_ending = self.x + 40
            self.y_ending = self.y + 40
            node = Node(self.canvas, creation, name_of_nodes[creation], self.x, self.y, self.x_ending, self.y_ending)
            self.Nodes_list.append(node)
            if creation % 2 == 0:
                self.x += 90
                self.y -= 30
            else:
                self.x -= 30
                self.y += 90
        self.sum = 0
        for e in tree.edges():
            self.starting_point = e[0] - 1
            self.ending_point = e[1] - 1
            self.weight = G.get_edge_data(self.starting_point + 1, self.ending_point + 1)["weight"]
            Edge(self.canvas, tree, self.Nodes_list[self.starting_point], self.Nodes_list[self.ending_point], self.weight)
            self.sum += G.get_edge_data(self.starting_point + 1, self.ending_point + 1)["weight"]
        self.canvas.create_text(195, 350, text=f"Weight : {self.sum}", font=("Arial Black", 20, "bold"), fill="black")
