import networkx as nx
import pandas as pd
import os

from entities.Graph import Graph
from methods.combine_odd_degree_node_pairs import combine_odd_degree_node_pairs
from methods.find_shortest_path_between_node_pairs import \
    find_shortest_path_between_node_pairs
from methods.get_kgraph_from_combined_pairs import \
    get_kgraph_from_combined_pairs
from methods.get_odd_degree_nodes import get_odd_degree_nodes
from methods.min_weight_matching import min_weight_matching
from methods.augment_original_graph import augment_original_graph
from methods.compute_eulerian_tour import compute_eulerian_tour
from methods.show_stats import show_stats, save_stats
from methods.plot_em_graph import plot_em_graph
from methods.plot_kgraph import plot_kgraph
from methods.plot_matching_kgraph import plot_matching_kgraph
from methods.plot_matching_kgraph_over_original_graph import \
    plot_matching_kgraph_over_original_graph

# > The class takes in a graph, finds the odd degree nodes, finds the shortest
# path between the odd degree nodes, finds the minimum weight matching between the
# odd degree nodes, augments the original graph with the minimum weight matching,
# and then finds the eulerian tour of the augmented graph


class ChinesePostmanProblem(Graph):
    def __init__(self, edges, nodes):
        """
        A constructor for the class. It initializes the class.

        :param edges: a list of tuples, where each tuple is an edge in the graph
        :param nodes: a list of nodes in the graph
        """
        super().__init__(edges, nodes)
        self._kgraph = None
        self._min_matching_edges = None
        self._augmented_graph = None
        self._eulerian_tour = None
        self._odd_degree_nodes = None

    def get_eulerian_tour(self):
        """
        It returns the eulerian tour of the graph.
        :return: The eulerian tour of the graph.
        """
        return self._eulerian_tour

    def get_odd_degree_nodes(self):
        """
        It returns the odd degree nodes.
        :return: The odd degree nodes.
        """
        return self._odd_degree_nodes

    def get_graph(self):
        """
        The function takes the nodes and edges dataframes and creates a graph object
        :return: A graph object
        """
        self._graph = nx.Graph()

        for i, elrow in self._edges.iterrows():
            self._graph.add_edge(elrow[0], elrow[1], **elrow[2:].to_dict())

        for i, nlrow in self._nodes.iterrows():
            nx.set_node_attributes(
                self._graph, {nlrow['id']:  nlrow[1:].to_dict()})

        return self._graph

    def compute(self, save=True):
        """
        We first find the odd degree nodes, then we combine them into pairs, then we
        find the shortest path between each pair, then we create a complete graph
        from the pairs, then we find the minimum weight matching, then we augment the
        original graph with the minimum weight matching, then we compute the eulerian
        tour

        :param save: If True, the solution will be saved to a file called stats.txt
        in the current working directory, defaults to True (optional)
        """
        if not self._graph:
            self.get_graph()

        self._odd_degree_nodes = get_odd_degree_nodes(graph=self._graph)
        odd_degree_pairs = combine_odd_degree_node_pairs(
            odd_degree_nodes=self._odd_degree_nodes)
        costs = find_shortest_path_between_node_pairs(
            graph=self._graph, odd_degree_pairs=odd_degree_pairs)
        self._kgraph = get_kgraph_from_combined_pairs(pair_weights=costs)
        self._min_matching_edges = min_weight_matching(kgraph=self._kgraph)
        self._augmented_graph = augment_original_graph(
            min_weight_pairs=self._min_matching_edges, graph=self._graph)

        self._eulerian_tour = compute_eulerian_tour(
            self._augmented_graph, self._graph)

        for i, edge in enumerate(self._eulerian_tour[0:50]):
            print(f'{i} | {edge[0]} -({edge[2]["weight"]})-> {edge[1]}')
        if save:
            with open(os.path.join(os.getcwd(), 'stats.txt'), 'w') as f:
                f.write(
                    f'Solution for graph with {len(self._graph.nodes)} nodes and {len(self._graph.edges)} edges: \n\n')
                for i, edge in enumerate(self._eulerian_tour):
                    f.write(
                        f'{i} | {edge[0]} -({edge[2]["weight"]})-> {edge[1]}\n')

    def plot(self):
        """
        > The function `plot()` plots the original graph, the k-graph, the minimum
        matching edges, and the minimum matching edges over the original graph
        """
        if not self._graph:
            self.get_graph()
        plot_em_graph(graph=self._graph)

        if not self._kgraph:
            self.compute()
        plot_kgraph(kgraph=self._kgraph, graph=self._graph)
        plot_matching_kgraph(
            matching_kgraph=self._min_matching_edges, kgraph=self._kgraph, graph=self._graph)
        plot_matching_kgraph_over_original_graph(
            self._min_matching_edges, self._graph)

    def solve(self, save=True):
        """
        > The function `solve` computes the solution of the problem, saves it, shows
        some statistics and plots the results

        :param save: if True, the results will be saved in a file, defaults to True
        (optional)
        """
        self.get_graph()
        self.compute(save)
        self.show_stats()
        self.plot()

    def show_stats(self):
        """
        It takes a graph and an eulerian tour of that graph and prints out the number
        of edges in the graph, the number of edges in the tour, and the number of
        edges that are in the graph but not in the tour
        """
        show_stats(self._eulerian_tour, self._graph)

    def save(self):
        """
        It saves the eulerian tour and the graph to a file.
        """
        save_stats(self._eulerian_tour, self._graph)
