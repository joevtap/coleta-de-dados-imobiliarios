from entities.Graph import Graph
from models import EM_EDGE_LIST, EM_NODE_LIST


def main():
    em_graph = Graph(edge_list=EM_EDGE_LIST, node_list=EM_NODE_LIST)
    em_graph.plot_graph()


if __name__ == "__main__":
    main()
