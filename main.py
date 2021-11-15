import networkx as nx

def init_visited(length: int):
    return [False for _ in range(length)]

def dfs(g: nx.Graph, node_idx: int) -> None:
    if visited[node_idx]:
        return
    visited[node_idx] = True
    for node in g.neighbors(node_idx+1):
        dfs(g, node - 1)
    
def findArticulationPoints(g: nx.Graph, graph_degree: int):
    global visited
    cut_nodes = []
    for i in range(graph_degree):
        ## remove node
        cloned = g.copy()
        cloned.remove_node(i+1)
        for j in range(graph_degree):
            if j != i:
                visited = init_visited(graph_degree)
                dfs(cloned, j)
                visited.pop(i)
                if not all(visited):
                    # i is an articulation point
                    if not i+1 in cut_nodes: 
                        cut_nodes.append(i+1)
    return cut_nodes
