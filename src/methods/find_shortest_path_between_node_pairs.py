from networkx import dijkstra_path_length


def find_shortest_path_between_node_pairs(odd_degree_pairs, graph):
    costs = {}
    for pair in odd_degree_pairs:
        costs[pair] = dijkstra_path_length(
            graph, pair[0], pair[1], weight='weight')
    return costs
