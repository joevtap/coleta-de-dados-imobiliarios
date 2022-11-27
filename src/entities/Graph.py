from abc import ABC, abstractmethod


class Graph:
    def __init__(self, edges, nodes):
        self._edges = edges
        self._nodes = nodes
        self._graph = None

    def get_edges(self):
        return self._edges

    def get_nodes(self):
        return self._nodes

    @abstractmethod
    def get_graph(self):
        pass

    @abstractmethod
    def compute(self):
        pass

    @abstractmethod
    def plot(self):
        pass
