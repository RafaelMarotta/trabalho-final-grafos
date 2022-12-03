import igraph as ig
import matplotlib.pyplot as plt
from igraph import Graph

from bridge_utils import *

class MyGraph:
    def __init__(self, n_vrt, directed=False, full=False):
        if full:
            self.g = Graph.Full(n=n_vrt, directed=directed)
        else:
            self.g = Graph(n=n_vrt, directed=directed)
        self.g.vs["label"] = range(self.g.vcount())
        self.g.vs["weight"] = self.g.vs["label"]

    def add_edge(self, v1, v2):
        self.g.add_edges([(v1, v2)])

    def remove_edge(self, v1, v2):
        self.g.delete_edges([(v1, v2)])

    def get_vertex_custom_attr(self, n_vertex, attr):
        return self.g.vs[n_vertex][attr]

    def set_vertex_custom_attr(self, n_vertex, attr, val):
        self.g.vs[n_vertex][attr] = val

    def get_vertex_label(self, n_vertex):
        return self.g.vs[n_vertex]["label"]

    def set_vertex_label(self, n_vertex, text):
        self.g.vs[n_vertex]["label"] = text

    def get_vertex_value(self, val):
        return self.g.vs[val]["weight"]

    def set_vertx_value(self, val):
        self.g.vs["weight"] = val

    def set_edge_label(self, text):
        self.g.es["label"] = text

    def set_edge_val(self, val):
        self.g.es["weight"] = val
        
    def get_edge_label(self):
        return self.g.es["label"]
    
    def get_edge_val(self):
        return self.g.es["weight"]
    
    def vertex_with_value_exists(self, v):
        for i in range(self.g.vcount()):
            if self.g.vs[i]["weight"] == v:
                return True
        return False

    def vertex_with_label_exists(self, v):
        for i in range(self.g.vcount()):
            if self.g.vs[i]["label"] == v:
                return True
        return False

    def get_adjacency_matrix(self):
        return self.g.get_adjacency()

    def get_adjacency_list(self):
        return self.g.get_adjlist()

    def is_vertices_adjacents(self, v1, v2):
        if self.g.are_connected(v1, v2):
            return True
        return False

    def is_edges_adjacents(self, v1, v2, v3, v4):
        return self.g.are_connected(v2, v3) or self.g.are_connected(v4, v1)

    def vertex_exists(self, v):
        return v in self.g.vs

    def vertex_count(self):
        return self.g.vcount()

    def edges_count(self):
        return self.g.ecount()

    def edge_exists(self, v1, v2):
        return self.g.are_connected(v1, v2)

    def is_graph_empty(self):
        return self.g.is_empty()

    def is_full_graph(self):
        for i in range(self.g.vcount()):
            if self.g.degree(i) != self.g.vcount() - 1:
                return False
        return True

    def has_bridge_tarjan(self):
        bridges = find_bridges_tarjan(self.g)
        return len(bridges) > 0

    def has_bridge_naive(self):
        bridges = find_bridges_naive(self.g)
        return len(bridges) > 0

    def is_bridge_tarjan(self, v1, v2):
        bridges = find_bridges_tarjan(self.g)
        return (v1, v2) in bridges

    def is_bridge_naive(self, v1, v2):
        bridges = find_bridges_naive(self.g)
        return (v1, v2) in bridges
    
    def fleury(self, method="TARJAN"):
        # Make sure the graph has either 0 or 2 odd vertices
        if not self.is_connected():
            return ["Não Euleriano"]
        odd_vertices = 0
        for i in range(self.g.vcount()):
            if self.g.degree(i) % 2 != 0:
                odd_vertices += 1
        if odd_vertices != 0 and odd_vertices != 2:
            return ["Não Euleriano"]

        # Make a copy of the graph
        g = self.g.copy()

        if (odd_vertices == 0):
            # If the graph has 0 odd vertices, pick any vertex
            start = i
        else:
            # If the graph has 2 odd vertices, pick the first one
            for i in range(g.vcount()):
                if g.degree(i) % 2 != 0:
                    start = i
                    break
        path = self.fleury_rec(g, start, [start], method="NAIVE")
        outp = "Euleriano" if path[0] == path[len(path) - 1] else "Semi-Euleriano"
        return [outp, path]
        
    def fleury_rec(self, g, v, path, method):
        if g.ecount() == 0:
            return path
        for e in self.g.get_adjlist()[v]:
           if not (self.is_bridge_tarjan(v, e) if method == "TARJAN" else self.is_bridge_naive(v, e)):
                break;
        g.delete_edges((v,e))
        path.append(e)
        return self.fleury_rec(g, e, path, method)
        
    def export_graph(self):
        self.g.write('graph.dot') 

    def import_graph(self, file, format):
        self.g = Graph.Read(file, format=format)
        pass

    def show(self):
        visual_style = {}
        visual_style["vertex_size"] = 0.5
        visual_style["vertex_color"] = "white"
        visual_style["edge_width"] = 0.5
        tx, ax = plt.subplots()
        ig.plot(self.g, target=ax, **visual_style)
        plt.show()
        
    def is_connected(self):
        return self.g.is_connected()