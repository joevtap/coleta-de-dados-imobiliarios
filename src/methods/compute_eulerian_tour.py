from networkx import eulerian_circuit, shortest_path


def compute_eulerian_tour(graph, graph_original):
    naive_tour = list(eulerian_circuit(graph, source=50))
    tour = []

    for edge in naive_tour:
        edge_data = graph.get_edge_data(edge[0], edge[1])

        if 'trail' not in edge_data[0]:
            edge_att = graph_original[edge[0]][edge[1]]
            tour.append((edge[0], edge[1], edge_att))
        else:
            aug_path = shortest_path(
                graph_original, edge[0], edge[1], weight='weight')
            aug_path_pairs = list(zip(aug_path[:-1], aug_path[1:]))

            for edge_aug in aug_path_pairs:
                edge_aug_att = graph_original[edge_aug[0]][edge_aug[1]]
                tour.append(
                    (edge_aug[0], edge_aug[1], edge_aug_att))

    return tour
