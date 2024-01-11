import networkx as nx
import matplotlib.pyplot as plt

def manual_edge_coloring(graph, manual_colors):
    colors = {}  # Dictionnaire pour stocker les couleurs assignées à chaque arête

    for edge in graph.edges():
        # Vérifiez si l'arête a une couleur manuelle attribuée
        if edge in manual_colors:
            colors[edge] = manual_colors[edge]
        else:
            colors[edge] = 'black'  # Couleur par défaut si aucune couleur manuelle n'est attribuée

    return colors

# Créer un graphe (exemple)
G = nx.Graph()
edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)]
G.add_edges_from(edges)

# Attribuer des couleurs manuelles à certaines arêtes
manual_colors = {(1, 2): 'red', (1, 3): 'blue', (2,3): 'green', (2,4): 'blue', (3,4): 'red', (4,5): 'green'}

# Appliquer la coloration aux arêtes du graphe
edge_colors = manual_edge_coloring(G, manual_colors)

# Dessiner le graphe avec les couleurs des arêtes
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=edge_colors.keys(), edge_color=list(edge_colors.values()))

# Afficher le graphe
plt.show()
