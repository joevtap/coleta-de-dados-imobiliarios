import networkx as nx


def augment_original_graph(graph, min_weight_pairs):
    """
    It takes a graph and a list of pairs of nodes, and adds edges between those
    pairs of nodes to the graph
    
    :param graph: the original graph
    :param min_weight_pairs: a list of tuples of the form (node1, node2)
    :return: The augmented graph is being returned.
    """
    augmented_graph = nx.MultiGraph(graph.copy())
    for pair in min_weight_pairs:
        augmented_graph.add_edge(pair[0],
                                 pair[1],
                                 **{'weight': nx.dijkstra_path_length(graph, pair[0], pair[1]), 'trail': 'augmented'}
                                 )
    return augmented_graph
