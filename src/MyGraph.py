import igraph as ig
import matplotlib.pyplot as plt
from igraph import Graph


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
        pass

    def get_vertex_custom_attr(self, n_vertex, attr):
        return self.g.vs[n_vertex][attr]

    def set_vertex_custom_attr(self, n_vertex, attr, val):
        self.g.vs[n_vertex][attr] = val

    def get_vertex_label(self, n_vertex):
        return

    def set_vertex_label(self, text):
        pass

    def get_vertex_value(self, val):
        pass

    def set_vertx_value(self, val):
        pass

    def set_edge_label(self, text):
        pass

    def set_edge_val(self, val):
        pass

    def vertex_with_value_exists(self, v):
        pass

    def vertex_with_label_exists(self, v):
        pass

    def get_adjacency_matrix(self):
        pass

    def get_adjacency_list(self):
        pass

    def is_vertices_adjacents(self, v1, v2):
        pass

    def is_edges_adjacents(self, v1, v2, v3, v4):
        pass

    def vertex_exists(self, v):
        pass

    def vertex_count(self):
        pass

    def edges_count(self):
        pass

    def edge_exists(self, v1, v2):
        pass

    def is_graph_empty(self):
        pass

    def is_full_graph(self):
        pass

    def has_bridge(self, method="TARJAN"):
        ## method = TARJAN/NAIVE
        pass

    def fleury(self, bridge_method="TARJAN"):
        pass

    def export_graph(self):
        # Checks out show method (That probably already solved this problem)
        pass

    def import_graph(file, format):
        # https://igraph.readthedocs.io/en/stable/generation.html#from-files
        pass

    def show(self):
        visual_style = {}
        visual_style["vertex_size"] = 0.5
        visual_style["vertex_color"] = "white"
        visual_style["edge_width"] = 0.5
        tx, ax = plt.subplots()
        ig.plot(self.g, target=ax, **visual_style)
        self.g.write('../out/graph.dot')  # Save a file
        plt.show()
