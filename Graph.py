from graph.prim import prim
from graph.kruskal import kruskal
from graph.bfs import bfs
from graph.dfs import dfs
from graph.directed.is_cyclic import is_cyclic as directed_is_cyclic
from graph.undirected.is_cyclic import is_cyclic as undirected_is_cyclic
import utils


class Graph:

    __nodes = set() # node ids
    __edges = {} # from node id to set of node ids

    def __init__(self, is_directed, weight_type):
        self.__is_directed = is_directed
        self.__weight_type = weight_type

    def add_node(self, node_id):
        self.__nodes.add(node_id)

    def add_edge(self, source_node_id, target_node_id, is_bidirectional=False):
        if source_node_id not in self.__edges:
            self.__edges[source_node_id] = set()

        self.__edges[source_node_id].add(target_node_id)

        if is_bidirectional:
            self.add_edge(target_node_id, source_node_id)

    def shortest_path_to_target(self, source_node_id, target_node_id):

    def shortest_path_to_all(self, source_node_id):

    def shortest_path_from_all_to_all(self):

    def is_cyclic(self):
        if self.__is_directed:
            directed_is_cyclic(self.__nodes, self.__edges)

        else:
            undirected_is_cyclic(self.__nodes, self.__edges)

    def minimum_spanning_tree(self):
        if self.__is_dense():
            return prim()
        else:
            return kruskal()

    def __is_dense(self):
        num_of_edges = len(utils.flatten(self.__edges))

        return num_of_edges > len(self.__nodes)

    def __bfs(self, source_node_id):
        bfs(self.__edges, source_node_id)

    def __dfs(self, source_node_id):
        dfs(self.__edges, source_node_id)








