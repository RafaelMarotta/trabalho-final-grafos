from MyGraph import MyGraph
import sys
from datetime import datetime

sys.setrecursionlimit(200000000)

# Representação utilizando Matriz/Lista de Adjacência

g = MyGraph(full=5, n_vrt=5)
print(g.get_adjacency_matrix())
print(g.get_adjacency_list())
g.show()

# Criação de grafos com X vértices
g = MyGraph(n_vrt=5)

# Adição de arestas
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
# g.show()

# Remoção de Arestas
g.remove_edge(2, 3)
# g.show()

# Ponderação de vértices
g = MyGraph(n_vrt=4)
g.set_vertex_label(0, "Rafael")
g.set_vertex_label(1, "Lucas")
g.set_vertex_label(2, "Lucas")
g.set_vertex_label(3, "Samuel")
# g.show()

# Ponderação de arestas
g = MyGraph(n_vrt=3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.set_edge_label(0, 1, "Teste")
g.set_edge_label(1, 2, "23/01")
g.get_edge_label(1, 2)
g.set_edge_val(1, 2, 5)
g.set_edge_val(1, 2, 10)
# g1.show()

# Checagem de adjacência entre vértices
g = MyGraph(n_vrt=3)
g.add_edge(0, 1)
g.add_edge(1, 2)
print(g.is_vertices_adjacents(0, 1))
print(g.is_vertices_adjacents(2, 0))

# Checagem de adjacência entre arestas
g = MyGraph(n_vrt=4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
print(g.is_edges_adjacents(0, 1, 1, 2))
print(g.is_edges_adjacents(0, 3, 2, 3))

# Checagem da existência de arestas
g = MyGraph(n_vrt=4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
print(g.edge_exists(0, 1))
print(g.edge_exists(1, 3))

# Checagem de quantidade de vértices e arestas
g = MyGraph(n_vrt=5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
print(g.vertex_count())
print(g.edges_count())

# Checagem de grafo vazio
g = MyGraph(n_vrt=5)
g.add_edge(0, 1)
print(g.is_graph_empty())
g.remove_edge(0, 1)
print(g.is_graph_empty())

# Checagem de grafo completo
g = MyGraph(n_vrt=5, full=True)
print(g.is_full_graph())
g.remove_edge(0, 1)
print(g.is_full_graph())

# Identifica ponte entre vértices
g = MyGraph(n_vrt=4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
print(g.is_bridge_naive(0, 1))
print(g.is_bridge_tarjan(0, 1))
print(g.is_bridge_naive(1, 3))
print(g.is_bridge_tarjan(1, 3))

# Fleury

# Exemplo Euleriano
g = MyGraph(n_vrt=5, full=True)
print(g.fleury())

# Exemplo Semi-Euleriano
g = MyGraph(n_vrt=4)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
print(g.fleury())

# Exemplo Não-Euleriano
g = MyGraph(n_vrt=4, full=True)
print(g.fleury())

#Teste com 100 vértices
g = MyGraph(n_vrt=100, ring=True)
print(datetime.today())
fleury = g.fleury(method="TARJAN")
print(datetime.today())
print(fleury)

# Teste com 1000 vértices
g = MyGraph(n_vrt=1000, n_edges=2450, random=True)
print(g.fleury())

# Teste com 10000 vértices
g = MyGraph(n_vrt=10000, n_edges=24047, random=True)
print(g.fleury())

# Teste com 100000 vértices
g = MyGraph(n_vrt=100000, n_edges=240035, random=True)
print(g.fleury())

# Export graph (Default: output.gml, format: gml)
## Nome do arquivo pode ser alterado pelo parâmetro filename e o formato pelo parâmetro format
g = MyGraph(n_vrt=5, full=True)
g.export_graph()

# Export graph (Default: output.gml, format: gml)
## Nome do arquivo pode ser alterado pelo parâmetro filename e o formato pelo parâmetro format
k5 = MyGraph().import_graph()
k5.show()