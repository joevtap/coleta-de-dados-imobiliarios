from models import EM_EDGE_LIST, EM_NODE_LIST
from entities.ChinesePostmanProblem import ChinesePostmanProblem


def main():
    em_cpp_problem = ChinesePostmanProblem(
        edges=EM_EDGE_LIST, nodes=EM_NODE_LIST)

    em_cpp_problem.solve()


if __name__ == "__main__":
    main()
