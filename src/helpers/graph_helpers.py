import networkx as nx
import matplotlib.pyplot as plt

def create_weighted_toy_graph():
    G = nx.Graph()
    # Add weighted edges to form two communities
    G.add_edge(0, 1, weight=10)  # Strong connection
    G.add_edge(1, 2, weight=10)  # Strong connection
    G.add_edge(0, 2, weight=1)   # Weak connection
    return G

def plot_weighted_graph(G, title=None, figsize=(3, 3), layout_seed=42, spacing=7):
    """
    Plots a weighted graph with edge labels.

    Parameters:
        G (networkx.Graph): The graph to plot.
        title (str): Title of the graph.
        figsize (tuple): Size of the figure (width, height).
        layout_seed (int): Seed for reproducible layout.
        spacing (float): Spacing between nodes in the layout.
    """
    # Compute layout
    pos = nx.spring_layout(G, seed=layout_seed, k=spacing)
    
    # Create figure
    plt.figure(figsize=figsize)
    
    # Draw nodes and edges
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', 
            node_size=500, font_size=10)
    
    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Add title and display
    plt.title(title)
    plt.show()

def create_toy_graph():
    G = nx.Graph()
    G.add_edges_from([[1,2], [2,3], [1,3], [1,4], [1,5], [3,5],
                  [6,7], [7,8], [8,9], [6,9], [6,8], [7,9],
                  [10,11], [11,12], [10,12],
                  [9,12], [2,7]])
    return G
