import networkx as nx
import matplotlib.pyplot as plt

# Créer un graphe orienté
G = nx.DiGraph()

# Ajouter des sommets
S = [1, 2, 3, 4, 5]
G.add_nodes_from(S)

# Ajouter des arêtes
A = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (3, 4), (5, 1), (5, 4)]
G.add_edges_from(A)

# Dessiner le graphe
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True, arrowsize=20)
plt.show()
