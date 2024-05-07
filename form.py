import tkinter as tk


def take_input(G):
    def create_root_2(no_of_edges):
        def submit_2():
            for edge_no in range(no_of_edges):
                edge = eval(edge_entry_list[edge_no].get())
                weight = int(weight_entry_list[edge_no].get())
                G.add_edge(edge[0], edge[1], weight=weight)
            root_2.destroy()

        root_2 = tk.Tk()
        root_2.title("Edge Inputs")
        edge_entry_list = []
        weight_entry_list = []
        for edge_input in range(no_of_edges):
            edge_label = tk.Label(root_2, text="Edge[Starting, Ending] : ", pady=10, padx=10)
            edge_label.grid(row=edge_input, column=0)
            edge_entry = tk.Entry(root_2)
            edge_entry.grid(row=edge_input, column=1, padx=10, pady=10)
            weight_label = tk.Label(root_2, text="Weight: ")
            weight_label.grid(row=edge_input, column=2)
            weight_entry = tk.Entry(root_2)
            weight_entry.grid(row=edge_input, column=3, pady=10, padx=10)
            edge_entry_list.append(edge_entry)
            weight_entry_list.append(weight_entry)
        submit_button = tk.Button(root_2, text="Enter", command=submit_2)
        submit_button.grid(row=no_of_edges, column=1)

        def on_enter(e):
            submit_button.config(bg="#D0E1F7")

        def on_leave(e):
            submit_button.config(bg='SystemButtonFace')

        submit_button.bind("<Enter>", on_enter)
        submit_button.bind("<Leave>", on_leave)

        root_2.mainloop()

    def submit_1():
        no_of_edges = int(edge_entry.get())
        root_1.destroy()
        create_root_2(no_of_edges)

    root_1 = tk.Tk()
    root_1.title("Nodes and Edges Entry")

    node_label = tk.Label(root_1, text="Number of Nodes:", padx=10, pady=10)
    node_label.grid(row=0, column=0)

    node_entry = tk.Entry(root_1)
    node_entry.grid(row=0, column=1, pady=10, padx=10)

    edge_label = tk.Label(root_1, text="Number of Edges:", pady=10, padx=10)
    edge_label.grid(row=1, column=0)

    edge_entry = tk.Entry(root_1)
    edge_entry.grid(row=1, column=1, pady=10, padx=10)

    submit_button = tk.Button(root_1, text="Enter", command=submit_1)
    submit_button.grid(row=2, column=1)

    def on_enter(e):
        submit_button.config(bg="#D0E1F7")

    def on_leave(e):
        submit_button.config(bg='SystemButtonFace')

    submit_button.bind("<Enter>", on_enter)
    submit_button.bind("<Leave>", on_leave)

    root_1.mainloop()
