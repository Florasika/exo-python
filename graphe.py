import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()


G.add_edge('1', '2', color='blue')
G.add_edge('1', '3', color='red')
G.add_edge('1', '4', color='blue')
G.add_edge('5', '4', color= 'red')
G.add_edge('1', '5', color='blue')
G.add_edge('5', '1', color='red')
G.add_edge('2', '3', color='blue')
G.add_edge('3', '4', color='red')


pos = nx.spring_layout(G)
edges = G.edges()
edge_colors = [G[u][v]['color'] for u, v in edges]
edge_labels = nx.get_edge_attributes(G, 'label')

nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', alpha=0.8)
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black', font_weight='bold')
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=edge_colors, arrowsize=20, connectionstyle='arc3,rad=0.1')

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

