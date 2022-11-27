import networkx as nx

from entities.Graph import Graph
from methods.combine_odd_degree_node_pairs import combine_odd_degree_node_pairs
from methods.find_shortest_path_between_node_pairs import \
    find_shortest_path_between_node_pairs
from methods.get_kgraph_from_combined_pairs import \
    get_kgraph_from_combined_pairs
from methods.get_odd_degree_nodes import get_odd_degree_nodes
from methods.min_weight_matching import min_weight_matching
from methods.plot_em_graph import plot_em_graph
from methods.plot_kgraph import plot_kgraph
from methods.plot_matching_kgraph import plot_matching_kgraph


class ChinesePostmanProblem(Graph):
    def __init__(self, edges, nodes):
        super().__init__(edges, nodes)
        self._kgraph = None
        self._matching_kgraph = None

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
        self._matching_kgraph = min_weight_matching(kgraph=self._kgraph)

    def plot(self):
        if not self._graph:
            self.get_graph()
        plot_em_graph(graph=self._graph)

        if not self._kgraph:
            self.compute()
        plot_kgraph(kgraph=self._kgraph, graph=self._graph)
        plot_matching_kgraph(
            matching_kgraph=self._matching_kgraph, kgraph=self._kgraph, graph=self._graph)

    def solve(self):
        pass
