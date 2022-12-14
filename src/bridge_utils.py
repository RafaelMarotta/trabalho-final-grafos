from igraph import Graph

def _tarjan_util(u, disc, low, parent, bridge, time, adj_list):
    disc[u] = time
    low[u] = time
    time += 1

    for v in adj_list[u]:
        
        if disc[v] == -1:
            parent[v] = u
            _tarjan_util(v, disc, low, parent, bridge, time, adj_list)

            low[u] = min(low[u], low[v])

            if low[v] > disc[u]:
                bridge.append((u, v))
            
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])

def find_bridges_tarjan(g: Graph):
    adj_list = g.get_adjlist()
    n = g.vcount()

    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n

    time = 0
    bridge = []

    for i in range(n):
        if disc[i] == -1:
            _tarjan_util(i, disc, low, parent, bridge, time, adj_list)

    return bridge

def find_bridges_naive(g: Graph):
    bridges = []
    adj_list = g.get_adjlist()

    for v1 in range(g.vcount()):
        for v2 in adj_list[v1]:
            g.delete_edges([(v1, v2)])
            if not g.is_connected():
                bridges.append((v1, v2))
            g.add_edges([(v1, v2)])
    return bridges
    
# Find height of a vertex 