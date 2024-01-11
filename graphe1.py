import matplotlib.pyplot as plt
import networkx as nx

# Définir un graphe pondéré
G = nx.Graph()

# Ajouter des arêtes avec des poids
edges = [
    ('x', 'A', 1),
    ('A', 'B', 1),
    ('x', 'C', 1),
    ('C', 'G', 1),
    ('G', 'H', 1),
    ('C', 'D', 1),
    ('D', 'E', 1),
    ('E', 'F', 1),
    ('A', 'G', 1),
    ('A', 'H', 1),
    ('B', 'H', 1),
    ('G', 'D', 1),
    ('G', 'E', 1),
    ('H', 'E', 1),
    ('H', 'F', 1),
    ('H', 'y', 1),
    ('F', 'y', 1),
    ('y', 'B', 1)
]

# Ajouter les arêtes au graphe
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Trouver la plus courte distance de x à y en utilisant l'algorithme de Moore
length, path = nx.single_source_bellman_ford(G, source='x', target='y')

# Afficher la plus courte distance et le chemin
print(f"La plus courte distance de x à y est {length} avec le chemin {path}.")

# Dessiner le graphe
pos = nx.spring_layout(G)  # Position des noeuds pour une meilleure apparence
weights = nx.get_edge_attributes(G, 'weight')  # Poids pour les labels des arêtes

# Dessiner les noeuds, arêtes et labels correspondants
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)


# Afficher le graphe
plt.show()
