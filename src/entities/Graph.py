from methods import generate_lists
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, edge_list, node_list):
        self.__edge_list = edge_list
        self.__node_list = node_list
        self.g = nx.Graph()
        self.generate_graph()

    def generate_graph(self):
        for i, elrow in self.__edge_list.iterrows():
            self.g.add_edge(elrow[0], elrow[1], **elrow[2:].to_dict())

        for i, nlrow in self.__node_list.iterrows():
            nx.set_node_attributes(self.g, {nlrow['id']:  nlrow[1:].to_dict()})

    def plot_graph(self):
        node_positions = {node[0]: (node[1]['x'], -node[1]['y'])
                          for node in self.g.nodes(data=True)}

        plt.figure(figsize=(8, 6))
        nx.draw(self.g, pos=node_positions, edge_color='black',
                node_size=10, node_color='black')
        plt.title('SOCORRO', size=15)
        plt.savefig('graph.png')

    def get_graph(self):
        return self.g
