import igraph as ig
import matplotlib.pyplot as plt
from igraph import Graph

from bridge_utils import find_bridges_tarjan

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
        pass

    def vertex_exists(self, v):
        if v in self.g.vs:
            return True
        return False

    def vertex_count(self):
        return self.g.vcount()

    def edges_count(self):
        return self.g.ecount()

    def edge_exists(self, v1, v2):
        pass

    def is_graph_empty(self):
        pass

    def is_full_graph(self):
        for i in range(self.g.vcount()):
            if self.g.degree(i) != self.g.vcount() - 1:
                return False
        return True        
    
    def has_bridge(self, method="TARJAN"):
        ## method = TARJAN/NAIVE
        pass

    def has_bridge_tarjan(self):
        bridges = find_bridges_tarjan(self.g)

        if len(bridges) > 0:
            return True

        return False

    def has_bridge_naive(self):
        # check method find_bridges_naive in tarjan.py
        pass

    def fleury(self, bridge_method="TARJAN"):
        pass

    def export_graph(self):
        # Checks out show method (That probably already solved this problem)
        pass

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
        self.g.write('graph.dot')  # Save a file
        plt.show()
        
    def is_connected(self):
        # https://igraph.org/python/doc/tutorial/tutorial.html#checking-whether-a-graph-is-connected
        if self.g.is_connected():
            return True
        return False

    