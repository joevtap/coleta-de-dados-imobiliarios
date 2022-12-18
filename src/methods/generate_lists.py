import os
from models import EM_ADJACENCY_MATRIX, nodes_coordinates


def generate_edge_list(adjacency_matrix, start_node=1, write_file=False):
    """
    It takes an adjacency matrix and returns a list of edges
    
    :param adjacency_matrix: The adjacency matrix of the graph
    :param start_node: The node number of the first node in the graph, defaults to 1
    (optional)
    :param write_file: If True, the generated edge list and node list will be
    written to a file, defaults to False (optional)
    :return: A list of dictionaries.
    """
    edge_list = []
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] != 0:
                edge_list.append({
                    'node_1': i + start_node,
                    'node_2': j + start_node,
                    'weight': adjacency_matrix[i][j],
                    'color': 'black'
                })

    if write_file:
        path = os.path.join(os.getcwd(), 'models', 'edge_list.py')
        with open(path, 'w') as file:
            file.write('edge_list = ' + str(edge_list))

    return edge_list


def generate_node_list(adjacency_matrix, start_node=1, write_file=False):
    node_list = []
    for i in range(len(adjacency_matrix)):
        node_list.append({
            'id': i + start_node,
            'x': nodes_coordinates.coordinates[i][0],
            'y': nodes_coordinates.coordinates[i][1]
        })

    if write_file:
        path = os.path.join(os.getcwd(), 'models', 'node_list.py')
        with open(path, 'w') as file:
            file.write('node_list = ' + str(node_list))

    return node_list
