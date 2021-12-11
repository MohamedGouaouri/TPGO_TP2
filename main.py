import networkx as nx





def init_visited(length: int):
    return [False for _ in range(length)]



def dfs(g: nx.Graph, node_idx: int, visited, mapping, reverse_mapping) -> None:
    if visited[node_idx]:
        return
    visited[node_idx] = True
    for node in g.neighbors(mapping[node_idx]):
        dfs(g, reverse_mapping[node], visited, mapping, reverse_mapping)
    return visited

def get_connexed_Graph_from_node(g : nx.Graph , nodeIndex : int , visitedNodes , all_nodes_visited):
    # global subgraph_nodes_visited
    if not(nodeIndex in visitedNodes):
        visitedNodes.append(nodeIndex)
        if not nodeIndex in all_nodes_visited:
            all_nodes_visited.append(nodeIndex)
        neighbors = g.neighbors(nodeIndex)
        for neighbor in neighbors:
            get_connexed_Graph_from_node(g , neighbor , visitedNodes , all_nodes_visited)

def get_connexed_Graphs_lists(g: nx.Graph):
    graphNodes=g.nodes()
    graphEdges=g.edges()
    all_nodes_visted=[]
    graphs=[]
    for nodeIndex in graphNodes:
        if not(nodeIndex in all_nodes_visted):
            visitedNodes=[]
            get_connexed_Graph_from_node(g , nodeIndex , visitedNodes , all_nodes_visted)
            new_g = nx.Graph()
            # print("visited Nodes =", visitedNodes)
            new_g.add_nodes_from(visitedNodes)
            for edgeTuple in graphEdges:
                if edgeTuple[0] in visitedNodes:
                    new_g.add_edge(edgeTuple[0],  edgeTuple[1])
            graphs.append(new_g)
    return graphs

def mapping(g):
    m = {}
    i = 0
    for node in g.nodes():
        m[i] = node
        i += 1
    return m
def reverse_mapping(g):
    m = {}
    i = 0
    for node in g.nodes():
        m[node] = i
        i += 1
    return m

def findArticulationPoints(g: nx.Graph, graph_degree: int):
    cut_nodes = []
    for i in range(graph_degree):
        ## remove node
        cloned = g.copy()
        m = mapping(g)
        rm = reverse_mapping(g)
        cloned.remove_node(m[i])
        
        for j in range(graph_degree):
            if j != i:
                visited = init_visited(graph_degree)
                dfs(cloned, j, visited, m, rm)
                visited.pop(i)
                if not all(visited):
                    # i is an articulation point
                    if not m[i] in cut_nodes:
                        cut_nodes.append(m[i])
    return cut_nodes



def main():
    g = nx.Graph()
    g.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    g.add_edges_from([(1, 2),(1, 3),(2, 3),(3, 4), (4, 5), (5, 6), (5, 7), (6, 7), (8, 9), (9, 10), (10, 11), (11, 12)])
    articulation_points = set()
    for subgraph in get_connexed_Graphs_lists(g):
        articulation_points = articulation_points.union(set(findArticulationPoints(subgraph, nx.number_of_nodes(subgraph))))
    print(set(list(nx.articulation_points(g))))
    print(articulation_points)


main()