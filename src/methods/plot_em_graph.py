import matplotlib.pyplot as plt
from networkx import draw


def plot_em_graph(graph):
    node_positions = {node[0]: (node[1]['x'], -node[1]['y'])
                      for node in graph.nodes(data=True)}

    greater_weight = max([edge[2]['weight']
                          for edge in graph.edges(data=True)])

    weights = [(graph[u][v]['weight'] / greater_weight)
               * 5 for u, v in graph.edges()]

    plt.figure(figsize=(16, 9))

    draw(graph, pos=node_positions, width=weights, edge_color='black',
         node_size=50, node_color='black')

    plt.savefig('graph.png')
