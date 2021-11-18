from networkx.classes.function import number_of_nodes
from .main import *
import pytest


def test1():
    g = nx.Graph()
    g.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
    g.add_edges_from([(1, 2), (2, 4), (2, 6), (6, 3), (6, 5), (3, 7)])

    cut_nodes = findArticulationPoints(g, number_of_nodes(g))
    assert sorted(list(nx.articulation_points(g))) == sorted(cut_nodes)


def test2():
    g = nx.Graph()
    g.add_nodes_from([1, 2, 3, 4, 5])
    g.add_edges_from([(1, 2), (2, 4), (4, 5), (3, 6), (3, 7), (6, 7)])
    graphs = get_connexed_Graphs_lists(g)
    # get_connexed_Graph_from_node(g , 1,  my_nodes , all_visited_nodes)
    print("\n",graphs)
    # cut_nodes = findArticulationPoints(g, number_of_nodes(g))
    # assert sorted(list(nx.articulation_points(g))) == sorted(cut_nodes)


def test3():
    g = nx.Graph()
    g.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
    g.add_edges_from([(1, 2), (2, 4), (2, 6), (6, 3), (6, 5), (3, 7)])

    cut_nodes = findArticulationPoints(g, number_of_nodes(g))
    assert sorted(list(nx.articulation_points(g))) == sorted(cut_nodes)


def test4():
    g = nx.Graph()
    g.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
    g.add_edges_from([(1, 2), (2, 4), (2, 6), (6, 3), (6, 5), (3, 7), (5, 7)])

    cut_nodes = findArticulationPoints(g, number_of_nodes(g))
    assert sorted(list(nx.articulation_points(g))) == sorted(cut_nodes)
