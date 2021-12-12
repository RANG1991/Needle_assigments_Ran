import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
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

