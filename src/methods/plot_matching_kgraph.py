import matplotlib.pyplot as plt
from networkx import draw, Graph


def plot_matching_kgraph(matching_kgraph, kgraph, graph):
    node_positions = {node[0]: (node[1]['x'], -node[1]['y'])
                      for node in graph.nodes(data=True)}

    plt.figure(figsize=(16, 9))

    draw(kgraph, pos=node_positions, node_size=20, alpha=0.05)

    kgraph_min_edges = Graph(matching_kgraph)
    draw(kgraph_min_edges, pos=node_positions,
         node_size=20, edge_color='red', node_color='black')

    plt.savefig('min_matching_kgraph.png', dpi=300)
    plt.clf()
