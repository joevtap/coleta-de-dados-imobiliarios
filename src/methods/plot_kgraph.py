import matplotlib.pyplot as plt
from networkx import draw_networkx_nodes, draw_networkx_edges, random_layout


def plot_kgraph(kgraph, graph):
    node_positions = {node[0]: (node[1]['x'], -node[1]['y'])
                      for node in graph.nodes(data=True)}

    plt.figure(figsize=(16, 9))
    pos_random = random_layout(kgraph)
    draw_networkx_nodes(kgraph, node_positions,
                        node_size=20, node_color="red")
    draw_networkx_edges(
        kgraph, node_positions, alpha=0.1)
    plt.axis('off')
    plt.savefig('kgraph.png')
