from models import EM_EDGE_LIST, EM_NODE_LIST, INSPECTOR_1_EDGES, INSPECTOR_1_NODES, INSPECTOR_2_EDGES, INSPECTOR_2_NODES
from entities.ChinesePostmanProblem import ChinesePostmanProblem
from entities.CPPSolution import CPPSolution


def main():
    # em_cpp_problem = ChinesePostmanProblem(
    #     edges=EM_EDGE_LIST, nodes=EM_NODE_LIST)

    em_cpp_problem = ChinesePostmanProblem(
        edges=INSPECTOR_2_EDGES, nodes=INSPECTOR_2_NODES)

    em_cpp_problem.solve()

    # em_cpp_solution = CPPSolution(
    #     nodes=EM_NODE_LIST, eulerian_tour=em_cpp_problem.get_eulerian_tour(), odd_degree_nodes=em_cpp_problem.get_odd_degree_nodes())

    em_cpp_solution = CPPSolution(
        nodes=INSPECTOR_2_NODES, eulerian_tour=em_cpp_problem.get_eulerian_tour(), odd_degree_nodes=em_cpp_problem.get_odd_degree_nodes())

    # em_cpp_solution.plot()
    em_cpp_solution.anim()


if __name__ == "__main__":
    main()
