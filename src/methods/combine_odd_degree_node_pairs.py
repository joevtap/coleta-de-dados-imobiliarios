import itertools


def combine_odd_degree_node_pairs(odd_degree_nodes):
    return list(itertools.combinations(odd_degree_nodes, 2))
