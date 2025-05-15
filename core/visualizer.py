# core/visualizer.py

import networkx as nx
import matplotlib.pyplot as plt

def build_memory_graph(memory_trace, symbol_table):
    G = nx.Graph()

    # Add nodes for each stimulus type
    for stim_type in symbol_table:
        label = symbol_table[stim_type]
        G.add_node(stim_type, label=label)

    # Add edges based on sequence co-occurrence
    for i in range(len(memory_trace) - 1):
        current = memory_trace[i]['stimulus']['type']
        next_ = memory_trace[i+1]['stimulus']['type']
        if current != next_:
            if G.has_edge(current, next_):
                G[current][next_]['weight'] += 1
            else:
                G.add_edge(current, next_, weight=1)

    return G

def draw_graph(G):
    pos = nx.spring_layout(G, seed=42)
    labels = {node: f"{data['label']}" for node, data in G.nodes(data=True)}
    edge_weights = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=False, node_color="#a0c4ff", node_size=1200, font_size=10)
    nx.draw_networkx_labels(G, pos, labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights)
    plt.title("Digital Mind: Memory Symbol Graph")
    plt.show()
