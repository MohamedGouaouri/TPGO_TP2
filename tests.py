from networkx.classes.function import number_of_nodes
from .main import *
import pytest


def test1():
    g = nx.Graph()
    g.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
    g.add_edges_from([(1, 2), (2, 4), (2, 6), (6, 3), (6, 5), (3, 7)])
    articulation_points = set()
    for subgraph in get_connexed_Graphs_lists(g):
        articulation_points = articulation_points.union(set(findArticulationPoints(subgraph, nx.number_of_nodes(subgraph))))
    
    assert set(list(nx.articulation_points(g))) == articulation_points

def test2():
    g = nx.Graph()
    g.add_nodes_from([1, 2, 3, 4, 5])
    g.add_edges_from([(1, 2), (2, 4), (4, 5), (3, 6), (3, 7), (6, 7), (8, 9)])
    articulation_points = set()
    for subgraph in get_connexed_Graphs_lists(g):
        articulation_points = articulation_points.union(set(findArticulationPoints(subgraph, nx.number_of_nodes(subgraph))))
    assert set(list(nx.articulation_points(g))) == articulation_points

def test3():
    g = nx.Graph()
    g.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
    g.add_edges_from([(1, 2), (2, 4), (2, 6), (6, 3), (6, 5), (3, 7)])
    articulation_points = set()
    for subgraph in get_connexed_Graphs_lists(g):
        articulation_points = articulation_points.union(set(findArticulationPoints(subgraph, nx.number_of_nodes(subgraph))))
    
    assert set(list(nx.articulation_points(g))) == articulation_points


def test4():
    g = nx.Graph()
    g.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
    g.add_edges_from([(1, 2), (2, 4), (2, 6), (6, 3), (6, 5), (3, 7), (5, 7)])
    articulation_points = set()
    for subgraph in get_connexed_Graphs_lists(g):
        articulation_points = articulation_points.union(set(findArticulationPoints(subgraph, nx.number_of_nodes(subgraph))))
    
    assert set(list(nx.articulation_points(g))) == articulation_points


def test5():
    g = nx.Graph()
    g.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    g.add_edges_from([(1, 2), (2, 4), (2, 6), (6, 3), (6, 5), (3, 7), (5, 7), (10,11), (9, 10)])
    articulation_points = set()
    for subgraph in get_connexed_Graphs_lists(g):
        articulation_points = articulation_points.union(set(findArticulationPoints(subgraph, nx.number_of_nodes(subgraph))))
    
    assert set(list(nx.articulation_points(g))) == articulation_points

def test6():
    g = nx.Graph()
    g.add_nodes_from([5, 6, 7, 8, 9, 10, 11])
    g.add_edges_from([(6, 5), (5, 7),(7,8), (10,11), (9, 10)])
    articulation_points = set()
    for subgraph in get_connexed_Graphs_lists(g):
        articulation_points = articulation_points.union(set(findArticulationPoints(subgraph, nx.number_of_nodes(subgraph))))
    
    assert set(list(nx.articulation_points(g))) == articulation_points


def test7():
    g = nx.Graph()
    g.add_nodes_from([11])
    articulation_points = set()
    for subgraph in get_connexed_Graphs_lists(g):
        articulation_points = articulation_points.union(set(findArticulationPoints(subgraph, nx.number_of_nodes(subgraph))))
    
    assert set(list(nx.articulation_points(g))) == articulation_points