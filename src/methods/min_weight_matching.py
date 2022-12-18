from networkx.algorithms import max_weight_matching
from pandas import unique


def min_weight_matching(kgraph):
    """
    It takes a graph and returns a list of edges that form a minimum weight matching
    
    :param kgraph: a networkx graph
    :return: A list of tuples of the form (k, v) where k and v are the nodes in the
    graph.
    """
    matches = max_weight_matching(kgraph, True)
    return list(unique([tuple(sorted([k, v]))
                        for k, v in matches]))
