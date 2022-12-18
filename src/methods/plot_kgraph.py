import matplotlib.pyplot as plt
from networkx import draw_networkx_nodes, draw_networkx_edges, random_layout


def plot_kgraph(kgraph, graph):
    """
    It takes a graph and a k-nearest-neighbor graph and plots the k-nearest-neighbor
    graph with the node positions of the original graph
    
    :param kgraph: the graph we're going to plot
    :param graph: the graph to be plotted
    """
    node_positions = {node[0]: (node[1]['x'], -node[1]['y'])
                      for node in graph.nodes(data=True)}

    plt.figure(figsize=(16, 9))
    pos_random = random_layout(kgraph)
    draw_networkx_nodes(kgraph, node_positions,
                        node_size=20, node_color="black")
    draw_networkx_edges(
        kgraph, node_positions, alpha=0.1)
    plt.axis('off')
    plt.savefig('kgraph.png', dpi=300)
    plt.clf()
