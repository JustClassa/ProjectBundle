#Project 26: Graph From Links

import networkx as nx
import matplotlib.pyplot as plt
from src.utils import custom_input

def proj_graph_from_links():
    """
    Constructs a graph using nodes and edges, either from user input or from provided parameters, 
    and visualizes the resulting graph using NetworkX and Matplotlib.
    
    A graph is a data structure made up of nodes (vertices) and links (edges). The representation
    can be useful for illustrating relationships between entities or analyzing network structures.
    
    Parameters:
        nodes (list, optional): A list of nodes to construct the graph. If None, user input is taken.
        edges (list of tuples, optional): A list of edges for the graph. If None, user input is taken.
    """
    nodes = custom_input("Enter the nodes separated by commas: ").split(',')
    edges = []
    while True:
        edge = custom_input("Enter an edge in the format 'node1,node2' (or press Enter to finish): ")
        if edge == '':
            break
        edges.append(tuple(edge.split(',')))

    graph = create_graph(nodes, edges)
    visualize_graph(graph)

def create_graph(nodes, edges):
    """
    Creates a NetworkX graph from the given nodes and edges.
    
    Parameters:
        nodes (list): List of nodes in the graph.
        edges (list of tuples): List of edges, where each edge is represented by a tuple of two nodes.
        
    Returns:
        G (networkx.Graph): The created graph.
    """
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G

def visualize_graph(graph):
    """
    Visualizes the given NetworkX graph using Matplotlib.
    
    Parameters:
        G (networkx.Graph): The graph to be visualized.
    """
    plt.figure(figsize=(10, 6))
    nx.draw(graph, with_labels=True, node_color='skyblue', node_size=500, font_size=10, font_weight='bold')
    plt.title("Graph from Links")
    plt.show()

if __name__ == "__main__":
    print("Testing Graph From Links Project")
    proj_graph_from_links()
