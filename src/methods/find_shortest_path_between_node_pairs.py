from networkx import dijkstra_path_length


def find_shortest_path_between_node_pairs(odd_degree_pairs, graph):
    """
    It takes a list of node pairs and a graph, and returns a dictionary of the
    shortest path lengths between each pair
    
    :param odd_degree_pairs: a list of tuples of the form (node1, node2)
    :param graph: the graph we're working with
    :return: A dictionary of the shortest path between each pair of nodes.
    """
    costs = {}
    for pair in odd_degree_pairs:
        costs[pair] = dijkstra_path_length(
            graph, pair[0], pair[1], weight='weight')
    return costs
