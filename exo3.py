import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Créer un graphe orienté
G = nx.DiGraph()

# Ajouter des sommets
S = [1, 2, 3]
G.add_nodes_from(S)

# Ajouter des arêtes
A = [(1, 2), (1, 3), (2, 1), (2, 3), (3, 2), (3, 3)]
#G.add_edges_from(A)
G.add_edge('1', '2', color='blue')
G.add_edge('1', '3', color='red')
G.add_edge('2','1', color='blue')
G.add_edge('2','3', color='red')
G.add_edge('3','2', color='green')
G.add_edge('3','3', color='red')


# Dessiner le graphe
#pos = nx.circular_layout(G)
#nx.draw(G, pos, with_labels=True, arrows=True, arrowsize=20)
#plt.show()


# Obtenir la matrice d'adjacence sous forme de tableau NumPy (matrice dense)
matrice = nx.to_numpy_array(G)

# Afficher la matrice d'adjacence
print("Matrice d'adjacence:")
print(matrice)

#Calculer la matrice à la puissance 4
M = np.linalg.matrix_power(matrice,4)
print(M)



# Calculer le nombre de cycles de longueur 4
nombre_circuit_longueur_4 = int(np.trace(M))  # Chaque cycle est compté deux fois
print(f"Le nombre de circuit de longueur 4 est {nombre_circuit_longueur_4}")





