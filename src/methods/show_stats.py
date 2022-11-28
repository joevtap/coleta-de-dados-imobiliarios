import networkx as nx
import pandas as pd


def show_stats(tour, graph):
    total_mileage_of_circuit = sum(
        [edge[2]['weight'] for edge in tour])
    total_mileage_on_orig_trail_map = sum(
        nx.get_edge_attributes(graph, 'weight').values())
    _vcn = pd.value_counts(pd.value_counts(
        [(e[0]) for e in tour]), sort=False)
    node_visits = pd.DataFrame(
        {'n_visits': _vcn.index, 'n_nodes': _vcn.values})
    _vce = pd.value_counts(pd.value_counts(
        [sorted(e)[0] + sorted(e)[1] for e in nx.MultiDiGraph(tour).edges()]))
    edge_visits = pd.DataFrame(
        {'n_visits': _vce.index, 'n_edges': _vce.values})

    # Printing stats
    print('Mileage of circuit: {0:.2f}'.format(total_mileage_of_circuit))
    print('Mileage on original trail map: {0:.2f}'.format(
        total_mileage_on_orig_trail_map))
    print('Mileage retracing edges: {0:.2f}'.format(
        total_mileage_of_circuit-total_mileage_on_orig_trail_map))
    print('Percent of mileage retraced: {0:.2f}%\n'.format(
        (1-total_mileage_of_circuit/total_mileage_on_orig_trail_map)*-100))

    print('Number of edges in circuit: {}'.format(len(tour)))
    print('Number of edges in original graph: {}'.format(len(graph.edges())))
    print('Number of nodes in original graph: {}\n'.format(len(graph.nodes())))

    print('Number of edges traversed more than once: {}\n'.format(
        len(tour)-len(graph.edges())))

    print('Number of times visiting each node:')
    print(node_visits.to_string(index=False))

    print('\nNumber of times visiting each edge:')
    print(edge_visits.to_string(index=False))
