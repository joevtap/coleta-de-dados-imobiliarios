from networkx import Graph


def get_kgraph_from_combined_pairs(pair_weights, flip_weights=True):
    """
    It takes a dictionary of pairs and their weights, and returns a graph with those
    pairs as edges
    
    :param pair_weights: a dictionary of pairs of nodes and their weights
    :param flip_weights: If True, the weights are flipped so that the shortest path
    is the one with the highest weight, defaults to True (optional)
    :return: A graph with the nodes and edges from the pair_weights dictionary.
    """
    new_g = Graph()

    for k, v in pair_weights.items():
        wt_i = -v if flip_weights else v
        new_g.add_edge(k[0], k[1], **{'cost': v, 'weight': wt_i})

    return new_g
