import os
from models import EM_ADJACENCY_MATRIX

def generate_edge_list(adjacency_matrix, start_node=1, write_file=False):
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
            'x': None,
            'y': None 
        })
    
    if write_file:
        path = os.path.join(os.getcwd(), 'models', 'node_list.py')
        with open(path, 'w') as file:
            file.write('node_list = ' + str(node_list))

    return node_list
