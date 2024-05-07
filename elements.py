from tkinter import Canvas


class Node(Canvas):
    def __init__(self, canvas, node_no, name, x_starting, y_starting, x_ending, y_ending):
        super().__init__()
        self.canvas = canvas
        self.x1 = x_starting
        self.y1 = y_starting
        self.x2 = x_ending
        self.y2 = y_ending
        self.name = name
        self.node_no = node_no
        self.text_x = self.x1 + 20
        self.text_y = self.y1 + 20
        self.draw()

    def draw(self):
        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="blue")
        self.canvas.create_text(self.text_x, self.text_y, text=self.name, font=("Arial Black", 20, "bold"), fill="white")


class Edge(Canvas):
    def __init__(self, canvas, G, node_1, node_2, weight):
        super().__init__()
        self.Graph = G
        self.canvas = canvas
        self.starting_x = node_1.x1 + 20
        self.starting_y = node_1.y1 + 20
        self.ending_x = node_2.x1 + 20
        self.ending_y = node_2.y1 + 20
        self.node_no = node_1.node_no
        self.weight = weight
        if self.node_no % 2 == 0:
            self.text_x = (self.starting_x + self.ending_x)/2 + 20
            self.text_y = (self.starting_y + self.ending_y) / 2
        else:
            self.text_x = (self.starting_x + self.ending_x) / 2
            self.text_y = (self.starting_y + self.ending_y) / 2 + 20
        self.draw()

    def draw(self):
        self.canvas.create_line(self.starting_x, self.starting_y, self.ending_x, self.ending_y)
        self.canvas.create_text(self.text_x, self.text_y, text=self.weight, font=("Arial Black", 10), fill="red")
