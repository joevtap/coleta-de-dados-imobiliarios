import itertools


def combine_odd_degree_node_pairs(odd_degree_nodes):
    """
    It takes a list of odd degree nodes and returns a list of all possible pairs of
    those nodes
    
    :param odd_degree_nodes: a list of nodes with odd degree
    :return: A list of tuples of all possible combinations of odd degree nodes.
    """
    return list(itertools.combinations(odd_degree_nodes, 2))
