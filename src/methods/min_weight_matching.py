from networkx.algorithms import max_weight_matching
from pandas import unique


def min_weight_matching(kgraph):
    matches = max_weight_matching(kgraph, True)
    return list(unique([tuple(sorted([k, v]))
                        for k, v in matches]))
