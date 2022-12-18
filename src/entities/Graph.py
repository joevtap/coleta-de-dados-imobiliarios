from abc import ABC, abstractmethod


class Graph:
    """
    > The Graph class is an abstract class that defines the basic structure of a
    graph
    """
    def __init__(self, edges, nodes):
        """
        The function takes in a list of edges and a list of nodes and creates a graph
        object
        
        :param edges: A list of tuples, where each tuple is of the form (node1,
        node2, weight)
        :param nodes: a list of nodes
        """
        self._edges = edges
        self._nodes = nodes
        self._graph = None

    def get_edges(self):
        """
        This function returns the edges of the graph
        :return: The edges of the graph.
        """
        return self._edges

    def get_nodes(self):
        """
        This function returns the nodes of the graph
        :return: The nodes are being returned.
        """
        return self._nodes

    @abstractmethod
    def get_graph(self):
        """
        `get_graph` is an abstract method that returns a graph
        """
        pass

    @abstractmethod
    def compute(self):
        """
        The function is an abstract method that is used to compute the value of the
        function
        """
        pass

    @abstractmethod
    def plot(self):
        """
        The function is an abstract method that is used to plot the data
        """
        pass
