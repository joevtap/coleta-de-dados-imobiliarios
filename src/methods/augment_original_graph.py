import networkx as nx


def augment_original_graph(graph, min_weight_pairs):
    augmented_graph = nx.MultiGraph(graph.copy())
    for pair in min_weight_pairs:
        augmented_graph.add_edge(pair[0],
                                 pair[1],
                                 **{'weight': nx.dijkstra_path_length(graph, pair[0], pair[1]), 'trail': 'augmented'}
                                 )
    return augmented_graph
