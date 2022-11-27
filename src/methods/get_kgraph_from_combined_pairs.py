from networkx import Graph


def get_kgraph_from_combined_pairs(pair_weights, flip_weights=True):
    new_g = Graph()

    for k, v in pair_weights.items():
        wt_i = -v if flip_weights else v
        new_g.add_edge(k[0], k[1], **{'cost': v, 'weight': wt_i})

    return new_g
