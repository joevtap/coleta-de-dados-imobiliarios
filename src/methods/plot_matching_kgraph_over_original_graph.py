import matplotlib.pyplot as plt
from networkx import draw, Graph, draw_networkx_edge_labels, draw_networkx_labels


def plot_matching_kgraph_over_original_graph(matching_kgraph, graph):
    node_positions = {node[0]: (node[1]['x'], -node[1]['y'])
                      for node in graph.nodes(data=True)}

    plt.figure(figsize=(16, 9))

    draw(graph, pos=node_positions, node_size=20,
         alpha=0.3, node_color='black')

    draw_networkx_edge_labels(graph, alpha=0.3, pos=node_positions, font_size=12,
                              edge_labels={(u, v): d['weight'] for u, v, d in graph.edges(data=True)})

    draw(Graph(matching_kgraph), pos=node_positions, node_size=20,
         alpha=1, node_color='black', edge_color='red', arrows=True, connectionstyle='arc3, rad=0.3')

    plt.savefig('min_matching_kgraph_over_original_graph.png', dpi=300)
    plt.clf()

    draw(graph, pos=node_positions, node_size=20,
         alpha=0.3, node_color='black')

    draw(Graph(matching_kgraph), pos=node_positions, node_size=20,
         alpha=1, node_color='black', edge_color='red', arrows=True, connectionstyle='arc3, rad=0.3')

    draw_networkx_labels(graph, pos=node_positions, font_size=12, alpha=1, verticalalignment='bottom', horizontalalignment='left',
                         labels={node[0]: node[0] for node in graph.nodes(data=True)})

    plt.savefig('min_matching_kgraph_over_original_graph_w_nodes.png', dpi=300)
    plt.clf()
