import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Créer un graphe orienté
G = nx.Graph()

# Ajouter des sommets
S = [1, 2, 3, 4]
G.add_nodes_from(S)

# Ajouter des arêtes
A = [(1, 3), (1, 4), (2, 3), (2, 4)]
G.add_edges_from(A)

# Dessiner le graphe
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()

# Obtenir la matrice d'adjacence sous forme de tableau NumPy (matrice dense)
adjacency_matrix = nx.to_numpy_array(G)

# Afficher la matrice d'adjacence
print("Matrice d'adjacence:")
print(adjacency_matrix)

#Calculer la matrice à la puissance 4
M = np.linalg.matrix_power(adjacency_matrix,4)
print(M)

print(f"le nombre de chaines de x1 à x2 est {M[0][1]}")
print(f"Le nombre de cycle de longueur 4 est {M.trace()}")
