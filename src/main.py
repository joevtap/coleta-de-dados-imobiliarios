from models import EM_EDGE_LIST, EM_NODE_LIST
from entities.ChinesePostmanProblem import ChinesePostmanProblem
from entities.CPPSolution import CPPSolution


def main():
    em_cpp_problem = ChinesePostmanProblem(
        edges=EM_EDGE_LIST, nodes=EM_NODE_LIST)

    em_cpp_problem.solve()

    em_cpp_solution = CPPSolution(
        nodes=EM_NODE_LIST, eulerian_tour=em_cpp_problem.get_eulerian_tour(), odd_degree_nodes=em_cpp_problem.get_odd_degree_nodes())

    # em_cpp_solution.plot()
    em_cpp_solution.anim()


if __name__ == "__main__":
    main()
