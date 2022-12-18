import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import copy
import os
import imageio

from entities.Graph import Graph


# It takes the eulerian tour and the nodes and creates a graph with the eulerian
# tour as edges and the nodes as nodes
class CPPSolution(Graph):
    def __init__(self, nodes, eulerian_tour, **kwargs):
        """
        The function takes in a list of nodes, an eulerian tour, and a list of odd
        degree nodes. It then creates a list of edges from the eulerian tour, and
        passes that list of edges, along with the list of nodes, to the parent
        class. It then sets the node positions to None, and sets the eulerian tour
        and odd degree nodes to the values passed in
        
        :param nodes: a list of nodes
        :param eulerian_tour: a list of nodes that form an eulerian tour of the
        graph
        """
        self._edges = self.get_cpp_edge_list(eulerian_tour)
        super().__init__(self._edges, nodes)
        self._node_positions = None
        self._eulerian_tour = eulerian_tour
        self._odd_degree_nodes = kwargs.get('odd_degree_nodes', None)

    def get_cpp_edge_list(self, eulerian_tour):
        """
        It takes the eulerian tour and returns a list of edges with the number of
        times each edge was visited and the sequence of the visits
        
        :param eulerian_tour: a list of tuples, where each tuple is an edge in the
        graph
        :return: A list of edges in the graph.
        """
        cpp_edgelist = {}

        for i, e in enumerate(eulerian_tour):
            edge = frozenset([e[0], e[1]])

            if edge in cpp_edgelist:
                cpp_edgelist[edge][2]['sequence'] += ', ' + str(i)
                cpp_edgelist[edge][2]['visits'] += 1

            else:
                cpp_edgelist[edge] = e
                cpp_edgelist[edge][2]['sequence'] = str(i)
                cpp_edgelist[edge][2]['visits'] = 1

        return list(cpp_edgelist.values())

    def get_graph(self):
        """
        It takes the nodes and edges dataframes and creates a networkx graph object.
        """
        self._graph = nx.Graph(self._edges)

        for i, nlrow in self._nodes.iterrows():
            nx.set_node_attributes(
                self._graph, {nlrow['id']:  nlrow[1:].to_dict()})

        self._node_positions = {node[0]: (node[1]['x'], -node[1]['y'])
                                for node in self._graph.nodes(data=True)}

    def compute(self):
        """
        It does nothing.
        """
        if not self._graph:
            self.get_graph()
        pass

    def plot(self):
        """
        It plots the graph with the edges colored according to the number of times
        they were visited, and then it plots the graph with the edges colored
        according to the sequence of the Eulerian path
        """
        if not self._graph:
            self.get_graph()

        plt.figure(figsize=(16, 9))

        visit_colors = {1: 'lightgray', 2: 'black'}
        edge_colors = [visit_colors[e[2]['visits']]
                       for e in self._graph.edges(data=True)]
        node_colors = [
            'black' if node in self._odd_degree_nodes else 'lightgray' for node in self._graph.nodes()]

        nx.draw_networkx(self._graph, pos=self._node_positions, node_size=20,
                         node_color=node_colors, edge_color=edge_colors, with_labels=True, verticalalignment='bottom', horizontalalignment='left', font_size=12)
        plt.axis('off')
        plt.savefig('cpp_solution.png', dpi=300)

        plt.clf()

        plt.figure(figsize=(16, 9))

        edge_colors = [e[2]['color'] for e in self._graph.edges(data=True)]
        nx.draw_networkx(self._graph, pos=self._node_positions, node_size=10, node_color='black',
                         edge_color=edge_colors, with_labels=True, alpha=0.5, verticalalignment='bottom', horizontalalignment='left', font_color='black', font_size=6)

        edge_labels = nx.get_edge_attributes(self._graph, 'sequence')
        nx.draw_networkx_edge_labels(
            self._graph, pos=self._node_positions, edge_labels=edge_labels, font_size=6, font_color='red')

        plt.axis('off')
        plt.savefig('cpp_solution_sequence.png', dpi=300)
        plt.clf()

    def anim(self):
        """
        It takes a graph, and for each edge in the graph, it draws the graph with
        the edges that have been walked so far, and then saves the image
        """
        if not self._graph:
            self.get_graph()

        image_path = os.path.join(os.getcwd(), 'fig', 'png')
        movie_filename = os.path.join(os.getcwd(), 'fig', 'movie.gif')
        fps = 3
        visit_colors = {1: 'black', 2: 'red'}
        edge_counter = {}
        g_i_edge_colors = []

        plt.clf()
        plt.figure(figsize=(16, 9))

        print('generating frames...')
        for i, e in enumerate(self._eulerian_tour, start=1):
            edge = frozenset([e[0], e[1]])
            if edge in edge_counter:
                edge_counter[edge] += 1
            else:
                edge_counter[edge] = 1

            # Full graph (faded in background)
            nx.draw_networkx(self._graph, pos=self._node_positions, node_size=6,
                             node_color='gray', with_labels=False, alpha=0.07)

            # Edges walked as of iteration i
            euler_tour_i = copy.deepcopy(self._eulerian_tour[0:i])
            for i in range(len(euler_tour_i)):
                edge_i = frozenset(
                    [euler_tour_i[i][0], euler_tour_i[i][1]])
                euler_tour_i[i][2]['visits_i'] = edge_counter[edge_i]
            g_i = nx.Graph(euler_tour_i)
            g_i_edge_colors = [visit_colors[e[2]['visits_i']]
                               for e in g_i.edges(data=True)]

            nx.draw_networkx_nodes(g_i, pos=self._node_positions, node_size=180, alpha=1,
                                   node_color='black', linewidths=0.1)
            nx.draw_networkx_edges(
                g_i, pos=self._node_positions, edge_color=g_i_edge_colors, alpha=0.8)

            edge_labels = nx.get_edge_attributes(self._graph, 'weight')
            nx.draw_networkx_edge_labels(
                g_i, pos=self._node_positions, edge_labels=edge_labels, font_size=6, font_color='red')

            nx.draw_networkx_labels(
                g_i, pos=self._node_positions, font_size=8, font_color='white', font_weight='bold')

            plt.axis('off')
            plt.savefig(f'fig/png/img{i}.png',
                        dpi=120, bbox_inches='tight')
            plt.clf()

        print('generating gif...')
        with imageio.get_writer('fig/gif/movie.gif', mode='i') as writer:
            for i in range(0, len(self._eulerian_tour)):
                image = imageio.imread(f'fig/png/img{i}.png')
                for _ in range(fps):
                    writer.append_data(image)
                writer.append_data(image)
