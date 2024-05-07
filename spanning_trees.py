from itertools import combinations
import networkx


def generate_spanning_trees(G):
    """
    Generate all possible spanning trees of a graph G.
    """
    num_nodes = len(G.nodes)
    spanning_trees = []

    # 'g' forms a graph using the list of edges.
    for edges in combinations(G.edges(), num_nodes-1):
        g = networkx.Graph(list(edges))
        if networkx.is_tree(g):
            spanning_trees.append(g)

    return spanning_trees
