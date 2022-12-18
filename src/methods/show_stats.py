import networkx as nx
import pandas as pd
import os


def show_stats(tour, graph):
    total_weight = sum(
        [edge[2]['weight'] for edge in tour])
    total_weight_original_trail = sum(
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
    print('Total edge cost of circuit: {0:.2f}'.format(total_weight))
    print('Total edge cost on original trail map: {0:.2f}'.format(
        total_weight_original_trail))
    print('Total edge cost retracing edges: {0:.2f}'.format(
        total_weight-total_weight_original_trail))
    print('Percent of mileage retraced: {0:.2f}%\n'.format(
        (1-total_weight/total_weight_original_trail)*-100))

    print('Number of edges in circuit: {}'.format(len(tour)))
    print('Number of edges in original graph: {}'.format(len(graph.edges())))
    print('Number of nodes in original graph: {}\n'.format(len(graph.nodes())))

    print('Number of edges traversed more than once: {}\n'.format(
        len(tour)-len(graph.edges())))

    print('Number of times visiting each node:')
    print(node_visits.to_string(index=False))

    print('\nNumber of times visiting each edge:')
    print(edge_visits.to_string(index=False))


def save_stats(tour, graph):
    total_weight = sum(
        [edge[2]['weight'] for edge in tour])
    total_weight_original_trail = sum(
        nx.get_edge_attributes(graph, 'weight').values())
    _vcn = pd.value_counts(pd.value_counts(
        [(e[0]) for e in tour]), sort=False)
    node_visits = pd.DataFrame(
        {'n_visits': _vcn.index, 'n_nodes': _vcn.values})
    _vce = pd.value_counts(pd.value_counts(
        [sorted(e)[0] + sorted(e)[1] for e in nx.MultiDiGraph(tour).edges()]))
    edge_visits = pd.DataFrame(
        {'n_visits': _vce.index, 'n_edges': _vce.values})

    local = os.path.join(os.getcwd(), 'stats.txt')

    # Saving stats
    with open('stats.txt', 'a') as f:
        f.write('\n\n')
        f.write('Total edge cost of circuit: {0:.2f}\n'.format(total_weight))
        f.write('Total edge cost on original trail map: {0:.2f}\n'.format(
            total_weight_original_trail))
        f.write('Total edge cost retracing edges: {0:.2f}\n'.format(
            total_weight-total_weight_original_trail))
        f.write('Percent of mileage retraced: {0:.2f}%\n\n'.format(
            (1-total_weight/total_weight_original_trail)*-100))
