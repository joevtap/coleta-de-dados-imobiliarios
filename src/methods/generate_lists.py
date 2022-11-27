from models import EM_ADJACENCY_MATRIX

def generate_edge_list(adjacency_matrix, start_node=1):
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

    return edge_list

def generate_node_list(adjacency_matrix, start_node=1):
    node_list = []
    for i in range(len(adjacency_matrix)):
        node_list.append({
            'id': i + start_node,
            'x': None, # TODO
            'y': None # TODO
        })

    return node_list
