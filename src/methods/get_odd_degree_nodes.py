def get_odd_degree_nodes(graph):
    nodes_odd_degree = [v for v, d in graph.degree() if d % 2 == 1]

    return nodes_odd_degree
