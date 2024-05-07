import networkx
from elements import Node, Edge
import tkinter as tk
from tkinter import ttk
from spanning_trees import generate_spanning_trees
from spanning_tree_GUI import Spanning_Tree_GUI
from minimum_spanning_tree import generate_mst
from form import take_input

name_of_nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
G = networkx.Graph()

choice = int(input("Give input using : \n1.GUI\n2.Terminal\nEnter your choice : "))

match(choice):
    case 1:
        take_input(G)
    case 2: 
        no_of_nodes = int(input("Enter the no. of nodes : "))
        no_of_edges = int(input("Enter the no. of edges : "))
        for edge in range(no_of_edges):
            edge_input = input(f"Enter the starting and ending vertices of edge {edge+1} : ")
            edge_input = eval(edge_input)
            weight = int(input("Enter the weight of the respective edge : "))
            if weight > 0:
                G.add_edge(edge_input[0], edge_input[1], weight=weight)

root = tk.Tk()
root.title("Graph")
root.geometry('500x500')
canvas = tk.Canvas(root, height=500, width=500)
Nodes_list = []

x = 35
y = 70
for node_no in range(len(G.nodes())):
    x_ending = x+40
    y_ending = y+40
    node = Node(canvas, node_no, name_of_nodes[node_no], x, y, x_ending, y_ending)
    Nodes_list.append(node)
    if node_no % 2 == 0:
        x += 150
        y -= 30
    else:
        x -= 30
        y += 140
# [[1,0], [2,0]]
for e in G.edges():
    starting_point = e[0] - 1
    ending_point = e[1] - 1
    weight = G.get_edge_data(starting_point+1, ending_point+1)["weight"]
    edge = Edge(canvas, G, Nodes_list[starting_point], Nodes_list[ending_point], weight)

spanning_trees = generate_spanning_trees(G)

mst_list = generate_mst(G, spanning_trees)

print("\nNumber of spanning trees : ", len(spanning_trees))
for T in spanning_trees:
    print(T.edges())


def draw_spanning_trees():
    root.destroy()
    root1 = tk.Tk()
    root1.geometry("1200x700")
    root1.configure(bg="white")

    full_canvas = tk.Canvas(root1, bg='white', highlightthickness=0)
    full_canvas.pack(side='left', fill='both', expand=True)

    inner_frame = tk.Frame(full_canvas, bg='white')
    inner_frame_id = full_canvas.create_window((0, 0), window=inner_frame, anchor='nw')

    row_no = 0
    column_no = 0
    for trees in spanning_trees:
        canvas1 = tk.Canvas(inner_frame, width=200, height=200, bg='white')
        canvas1.grid(row=row_no, column=column_no, sticky="NSEW")
        canvas1.config(width=400, height=400)
        Spanning_Tree_GUI(trees, canvas1, G)
        column_no += 1
        if column_no == 3:
            row_no += 1
            column_no = 0
    scrollbar = ttk.Scrollbar(root1, orient='vertical', command=full_canvas.yview)
    scrollbar.pack(side='right', fill='y')
    full_canvas.configure(yscrollcommand=scrollbar.set)

    def update_canvas(event):
        full_canvas.configure(scrollregion=full_canvas.bbox('all'))

    full_canvas.bind('<Configure>', update_canvas)

    def update_inner_frame(event):
        full_canvas.itemconfigure(inner_frame_id, height=inner_frame.winfo_reqheight())

    inner_frame.bind('<Configure>', update_inner_frame)
    root1.title("All Possible Spanning Trees")

    generate_mst = ttk.Button(root1, text="Generate all minimum spanning trees", command=draw_minimum_spanning_trees, width=40)
    generate_mst.place(x=500, y=650)
    no_spanning_trees = ttk.Label(full_canvas, text=f"No. of Spanning Trees = {len(spanning_trees)}", font=("Arial Black", 15, "bold"), background="White")
    no_spanning_trees.place(x=120, y=0)
    no_spanning_trees.pack()
    root1.mainloop()


def draw_minimum_spanning_trees():
    root2 = tk.Tk()
    root2.geometry("1200x650")
    root2.columnconfigure(0, weight=1)
    root2.rowconfigure(0, weight=1)

    full_canvas = tk.Canvas(root2, bg='white', highlightthickness=0)
    full_canvas.pack(side='left', fill='both', expand=True)

    inner_frame = tk.Frame(full_canvas, bg='white')
    inner_frame_id = full_canvas.create_window((0, 0), window=inner_frame, anchor='nw')

    row_no = 0
    column_no = 0
    for trees in mst_list:
        canvas1 = tk.Canvas(inner_frame, width=200, height=200, bg='white')
        canvas1.grid(row=row_no, column=column_no, sticky="NSEW")
        canvas1.config(width=400, height=400)
        Spanning_Tree_GUI(trees, canvas1, G)
        column_no += 1
        if column_no == 3:
            row_no += 1
            column_no = 0
    scrollbar = ttk.Scrollbar(root2, orient='vertical', command=full_canvas.yview)
    scrollbar.pack(side='right', fill='y')
    full_canvas.configure(yscrollcommand=scrollbar.set)

    def update_canvas(event):
        full_canvas.configure(scrollregion=full_canvas.bbox('all'))

    full_canvas.bind('<Configure>', update_canvas)

    def update_inner_frame(event):
        full_canvas.itemconfigure(inner_frame_id, height=inner_frame.winfo_reqheight())

    inner_frame.bind('<Configure>', update_inner_frame)
    no_mst = ttk.Label(full_canvas, text=f"No. of Minimum Weight Spanning Trees = {len(mst_list)}", font=("Arial Black", 15, "bold"), background="White")
    no_mst.place(x=120, y=0)
    no_mst.pack()
    root2.title("All Possible Minimum weight spanning Trees")
    root2.mainloop()


generate = ttk.Button(root, text="Generate", command=draw_spanning_trees)
cancel = ttk.Button(root, text="Cancel", command=root.destroy)
cancel.pack(side="bottom")
generate.pack(side="bottom")
canvas.pack(expand=True)
root.mainloop()
