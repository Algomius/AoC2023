import networkx as nx

g = nx.Graph()

f = open("input25.txt", "r")
for x in f:
    x  = x[:-1]
    left, right = x.split(":")
    for node in right.strip().split():
        g.add_edge(left, node)
        g.add_edge(node, left)

g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)
print(len(a) * len(b))
