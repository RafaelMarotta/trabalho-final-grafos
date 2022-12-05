import igraph as ig
import matplotlib.pyplot as plt
from igraph import Graph

from bridge_utils import *


class MyGraph:
    def __init__(self, g=None, n_vrt=None, n_edges=None, directed=False, full=False, random=False, ring=False):
        if g is not None:
            self.g = g
        elif ring:
            self.g = Graph.Ring(n_vrt, directed=directed)
        elif random:
            # Generate a random graph with n_vrt vertices and n_edges edges with loop disabled and parallel
            self.g = Graph.Erdos_Renyi(n=n_vrt, m=n_edges, directed=directed, loops=False)
        elif full:
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

    def set_vertex_value(self, n_vertex, val):
        self.g.vs[n_vertex]["weight"] = val

    def set_edge_label(self, v1, v2, text):
        self.g.es[self.g.get_eid(v1, v2)]["label"] = text

    def set_edge_val(self,  v1, v2, val):
        self.g.es[self.g.get_eid(v1, v2)]["weight"] = val

    def get_edge_label(self,  v1, v2):
        return self.g.es[self.g.get_eid(v1, v2)]["label"]

    def get_edge_val(self,  v1, v2):
        return self.g.es[self.g.get_eid(v1, v2)]["weight"]

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
        return self.g.are_connected(v2, v4) and self.g.are_connected(v1, v2) or self.g.are_connected(v1, v4) and self.g.are_connected(v3, v4)

    def vertex_exists(self, v):
        return v in self.g.vs

    def edge_exists(self, v1, v2):
        return self.g.are_connected(v1, v2)

    def vertex_count(self):
        return self.g.vcount()

    def edges_count(self):
        return self.g.ecount()


    def is_graph_empty(self):
        return self.g.ecount() == 0 and self.g.vcount() > 0

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

    def clone(self):
        return MyGraph(g=self.g.copy())

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
        graph = self

        if (odd_vertices == 0):
            # If the graph has 0 odd vertices, pick any vertex
            start = i
        else:
            # If the graph has 2 odd vertices, pick the first one
            for i in range(graph.g.vcount()):
                if graph.g.degree(i) % 2 != 0:
                    start = i
                    break
        path = graph.fleury_rec(graph, start, [start], method=method)
        outp = "Euleriano" if path[0] == path[len(
            path) - 1] else "Semi-Euleriano"
        return [outp, path]

    def fleury_rec(self, graph, v, path, method):
        if graph.g.ecount() == 0:
            return path
        for e in graph.g.get_adjlist()[v]:
            if not (graph.is_bridge_tarjan(v, e) if method == "TARJAN" else graph.is_bridge_naive(v, e)):
                break
        graph.g.delete_edges([(v, e)])
        path.append(e)
        return graph.fleury_rec(graph, e, path, method)

    def export_graph(self, filename="output.gml", format="gml"):
        ## Export graph to file on graphml format
        self.g.write(filename, format)

    def import_graph(self, filename="output.gml", format="gml"):
        ## Import graph from file on graphml format
        return MyGraph(g= Graph.Load(filename, format=format))

    def show(self):
        visual_style = {}
        visual_style["vertex_size"] = 0.5
        visual_style["vertex_color"] = "white"
        visual_style["edge_width"] = 0.5
        visual_style["edge_color"] = "black"
        visual_style["edge_size"] = 0.1
        visual_style["edge_align_label"] = True

        tx, ax = plt.subplots()
        ig.plot(self.g, layout="kk", target=ax, **visual_style)
        plt.show()

    def is_connected(self):
        return self.g.is_connected()
