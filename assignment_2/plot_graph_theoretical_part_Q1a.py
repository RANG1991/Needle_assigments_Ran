import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from(
    [('A', 'B'),
     ('A', 'C'),
     ('B', 'C'),
     ('B', 'H'),
     ('C', 'D'),
     ('H', 'I'),
     ('H', 'G'),
     ('D', 'E'),
     ('D', 'F'),
     ('I', 'G'),
     ('G', 'E'),
     ('E', 'F')
     ])

for node in G.nodes:
    edges = list(nx.edge_bfs(G, node))
    G_temp = nx.Graph()
    G_temp.add_edges_from(edges)
    pos = nx.spring_layout(G_temp)
    nx.draw(G_temp, pos, with_labels=True, cmap=plt.get_cmap('jet'), node_size=500)
    plt.show()
