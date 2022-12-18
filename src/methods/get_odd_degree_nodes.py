def get_odd_degree_nodes(graph):
    """
    It takes in a graph and returns a list of nodes with odd degree
    
    :param graph: a networkx graph
    :return: A list of nodes with odd degree.
    """
    nodes_odd_degree = [v for v, d in graph.degree() if d % 2 == 1]

    return nodes_odd_degree
