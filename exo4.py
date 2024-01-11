import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Créer un graphe orienté
G = nx.DiGraph()

# Ajouter des sommets
S = [1, 2, 3]
G.add_nodes_from(S)

# Ajouter des arêtes
A = [(1, 2), (1, 3), (2, 1), (2, 3), (3, 3)]
G.add_edges_from(A)



# Dessiner le graphe
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True, arrowsize=20)
plt.show()

#calculer la matrice de distance
distance_matrix = nx.floyd_warshall_numpy(G)
num_nodes = len(G.nodes)
distance_matrix_str = [[
