from MyGraph import MyGraph

# Have fun guys =)


def example_not_directed_graph():
    g = MyGraph(3)  # Create a new graph with 5 vertices
    g.add_edge(0, 1)
    g.add_edge(1, 2)

    g.show()
    ret = g.fleury()
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
    g = MyGraph(5, directed=True)
    g.show()

def example_adjacency_matrix():
    g = MyGraph(1, directed=False, full=False)
    g.show()
    print(g.import_graph())
    print(g.get_adjacency_matrix())

example_not_directed_graph()