import networkx as nx

# graphs=[]
# all_nodes_visted=[]
# subgraph_nodes_visited=[]

def init_visited(length: int):
    return [False for _ in range(length)]



def dfs(g: nx.Graph, node_idx: int) -> None:
    if visited[node_idx]:
        return
    visited[node_idx] = True
    for node in g.neighbors(node_idx + 1):
        dfs(g, node - 1)
    print("VISITED = ", visited)

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
    all_nodes_visted=[]
    graphs=[]
    for nodeIndex in graphNodes:
        if not(nodeIndex in all_nodes_visted):
            visitedNodes=[]
            get_connexed_Graph_from_node(g , nodeIndex , visitedNodes , all_nodes_visted)
            graphs.append(visitedNodes)
    return graphs

def findArticulationPoints(g: nx.Graph, graph_degree: int):
    global visited
    cut_nodes = []
    for i in range(graph_degree):
        ## remove node
        cloned = g.copy()
        cloned.remove_node(i + 1)
        for j in range(graph_degree):
            if j != i:
                visited = init_visited(graph_degree)
                dfs(cloned, j)
                visited.pop(i)
                if not all(visited):
                    # i is an articulation point
                    if not i + 1 in cut_nodes:
                        cut_nodes.append(i + 1)
    return cut_nodes
