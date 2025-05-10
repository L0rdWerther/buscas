import matplotlib.pyplot as plt
import networkx as nx

# Define o grafo
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1), ('E', 8)],
    'D': [('B', 5), ('C', 1), ('E', 2), ('F', 6)],
    'E': [('C', 8), ('D', 2), ('F', 3), ('G', 7)],
    'F': [('D', 6), ('E', 3), ('G', 2), ('H', 5)],
    'G': [('E', 7), ('F', 2), ('H', 1), ('I', 4)],
    'H': [('F', 5), ('G', 1), ('I', 3), ('J', 2)],
    'I': [('G', 4), ('H', 3), ('J', 6), ('K', 5)],
    'J': [('H', 2), ('I', 6), ('K', 4), ('L', 7)],
    'K': [('I', 5), ('J', 4), ('L', 3), ('M', 6)],
    'L': [('J', 7), ('K', 3), ('M', 2), ('N', 8)],
    'M': [('K', 6), ('L', 2), ('N', 4)],
    'N': [('L', 8), ('M', 4)]
}

G = nx.Graph()
for node, neighbors in grafo.items():
    for neighbor, weight in neighbors:
        G.add_edge(node, neighbor, weight=weight)

# Desenho do grafo
pos = nx.spring_layout(G, seed=42)  # Posição dos nós
edge_labels = nx.get_edge_attributes(G, 'weight')

plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)
plt.title("Grafo com Pesos nas Arestas")
plt.axis('off')
plt.tight_layout()
plt.show()
