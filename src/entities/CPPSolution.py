import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import copy
import os
import imageio

from entities.Graph import Graph


class CPPSolution(Graph):
    def __init__(self, nodes, eulerian_tour, **kwargs):
        self._edges = self.get_cpp_edge_list(eulerian_tour)
        super().__init__(self._edges, nodes)
        self._node_positions = None
        self._eulerian_tour = eulerian_tour
        self._odd_degree_nodes = kwargs.get('odd_degree_nodes', None)

    def get_cpp_edge_list(self, eulerian_tour):
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
        self._graph = nx.Graph(self._edges)

        for i, nlrow in self._nodes.iterrows():
            nx.set_node_attributes(
                self._graph, {nlrow['id']:  nlrow[1:].to_dict()})

        self._node_positions = {node[0]: (node[1]['x'], -node[1]['y'])
                                for node in self._graph.nodes(data=True)}

    def compute(self):
        if not self._graph:
            self.get_graph()
        pass

    def plot(self):
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
