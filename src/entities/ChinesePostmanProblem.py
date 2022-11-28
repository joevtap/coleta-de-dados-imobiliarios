import networkx as nx
import pandas as pd

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
from methods.show_stats import show_stats
from methods.plot_em_graph import plot_em_graph
from methods.plot_kgraph import plot_kgraph
from methods.plot_matching_kgraph import plot_matching_kgraph
from methods.plot_matching_kgraph_over_original_graph import \
    plot_matching_kgraph_over_original_graph


class ChinesePostmanProblem(Graph):
    def __init__(self, edges, nodes):
        super().__init__(edges, nodes)
        self._kgraph = None
        self._min_matching_edges = None
        self._augmented_graph = None
        self._eulerian_tour = None

    def get_graph(self):
        self._graph = nx.Graph()

        for i, elrow in self._edges.iterrows():
            self._graph.add_edge(elrow[0], elrow[1], **elrow[2:].to_dict())

        for i, nlrow in self._nodes.iterrows():
            nx.set_node_attributes(
                self._graph, {nlrow['id']:  nlrow[1:].to_dict()})

        return self._graph

    def compute(self):
        if not self._graph:
            self.get_graph()

        odd_degree_nodes = get_odd_degree_nodes(graph=self._graph)
        odd_degree_pairs = combine_odd_degree_node_pairs(
            odd_degree_nodes=odd_degree_nodes)
        costs = find_shortest_path_between_node_pairs(
            graph=self._graph, odd_degree_pairs=odd_degree_pairs)
        self._kgraph = get_kgraph_from_combined_pairs(pair_weights=costs)
        self._min_matching_edges = min_weight_matching(kgraph=self._kgraph)
        self._augmented_graph = augment_original_graph(
            min_weight_pairs=self._min_matching_edges, graph=self._graph)

        self._eulerian_tour = compute_eulerian_tour(
            self._augmented_graph, self._graph)

    def plot(self):
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

    def solve(self):
        self.get_graph()
        self.compute()
        # show_stats(self._eulerian_tour, self._graph)
        self.plot()
