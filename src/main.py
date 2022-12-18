from models import EM_EDGE_LIST, EM_NODE_LIST, INSPECTOR_1_EDGES, INSPECTOR_1_NODES, INSPECTOR_2_EDGES, INSPECTOR_2_NODES
from entities.ChinesePostmanProblem import ChinesePostmanProblem
from entities.CPPSolution import CPPSolution

edges = EM_EDGE_LIST
nodes = EM_NODE_LIST


def main():
    em_cpp_problem = ChinesePostmanProblem(
        edges=edges, nodes=nodes)

    em_cpp_problem.solve(save=True)

    em_cpp_solution = CPPSolution(
        nodes=nodes, eulerian_tour=em_cpp_problem.get_eulerian_tour(), odd_degree_nodes=em_cpp_problem.get_odd_degree_nodes())

    em_cpp_problem.plot()
    em_cpp_problem.save()
    # em_cpp_solution.anim()


if __name__ == "__main__":
    main()
