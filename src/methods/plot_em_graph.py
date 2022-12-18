import matplotlib.pyplot as plt
from networkx import draw, draw_networkx_edge_labels


def plot_em_graph(graph):
    """
    It takes a graph, finds the maximum weight of all edges, then plots the graph
    with the width of each edge proportional to its weight
    
    :param graph: the graph to be plotted
    """
    node_positions = {node[0]: (node[1]['x'], -node[1]['y'])
                      for node in graph.nodes(data=True)}

    greater_weight = max([edge[2]['weight']
                          for edge in graph.edges(data=True)])

    weights = [(graph[u][v]['weight'] / greater_weight)
               * 5 for u, v in graph.edges()]

    plt.figure(figsize=(16, 9))

    draw(graph, pos=node_positions, width=weights, edge_color='black',
         node_size=50, node_color='black')

    draw_networkx_edge_labels(graph, pos=node_positions, font_size=12,
                              edge_labels={(u, v): d['weight'] for u, v, d in graph.edges(data=True)})

    plt.savefig('graph.png', dpi=300)
    plt.clf()
