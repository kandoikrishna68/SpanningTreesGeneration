import networkx


def generate_mst(G, spanning_trees):
    mst = networkx.Graph()
    mst_weight = 0
    start_node = next(iter(G.nodes()))
    visited = {start_node}
    while len(visited) < len(G.nodes()):
        min_edge = None
        min_weight = float('inf')
        for u in visited:
            for v in G.nodes():
                if v not in visited and G.has_edge(u, v):
                    weight = G.edges[u, v]["weight"]
                    if weight < min_weight:
                        min_edge = (u, v)
                        min_weight = weight
        u, v = min_edge
        mst.add_edge(u, v, weight=min_weight)
        mst_weight += min_weight
        visited.add(v)
    print("\nWeight : ", mst_weight)
    mst_list = []
    for tree in spanning_trees:
        weight = 0
        for e in tree.edges():
            weight += G.edges[e]["weight"]
        if weight == mst_weight:
            mst_list.append(tree)
    print(f"Number of minimum weight spanning trees: {len(mst_list)}")
    for tree in mst_list:
        for e in tree.edges():
            print(e, end=" ")
        print()

    return mst_list
