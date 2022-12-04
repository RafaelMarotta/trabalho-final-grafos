from MyGraph import MyGraph

# Have fun guys =)


def example_not_directed_graph():
    g = MyGraph(n_vrt = 50, n_edges=500, random=True)  # Create a new graph with 5 vertices

    #g.show()
    ret = g.fleury()
    print(ret[0])
    while ret[0] is not "Euleriano":
        g = MyGraph(n_vrt = 10, n_edges=20, random=True)
        ret = g.fleury(method="NAIVE")
        print(ret[0])
    print(ret[1])


def example_directed_graph():
    g = MyGraph(3, directed=True)
    g.add_edge(0, 1)  # Create an edge from vertex 0 to vertex 1
    g.add_edge(0, 2)  # Create an edge from vertex 1 to vertex 2
    g.show()


def example_of_label():
    g = MyGraph(1)
    g.set_vertex_custom_attr(0, "label", "Hello World")
    print(g.get_vertex_custom_attr(0, "label"))
    g.show()


def example_full_graph():
    g = MyGraph(100000, directed=False)
    g.show()

def example_adjacency_matrix():
    g = MyGraph(1, directed=False, full=False)
    g.show()
    print(g.import_graph())
    print(g.get_adjacency_matrix())

example_not_directed_graph()
#g = MyGraph.import_graph("./graph.dot", format="graphml")
#g.show

