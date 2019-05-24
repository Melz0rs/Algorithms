from graph.algorithms.prim import prim
from graph.algorithms.kruskal import kruskal
from graph.algorithms.bfs import bfs
from graph.algorithms.dfs import dfs
from graph.directed.is_cyclic import is_cyclic as directed_is_cyclic
from graph.undirected.is_cyclic import is_cyclic as undirected_is_cyclic
from graph.Edge import Edge
import graph.graph_utils as graph_utils
import utils


class Graph:

    __nodes = set() # node ids
    __edges = {} # from node id to set of edges

    def __init__(self, is_directed, weight_type=None):
        self.__is_directed = is_directed
        self.__weight_type = weight_type

    def add_node(self, node_id):
        self.__nodes.add(node_id)

    def add_edge(self, source_id, target_id, weight):
        if source_id not in self.__nodes:
            self.__nodes.add(source_id)

        if target_id not in self.__nodes:
            self.__nodes.add(target_id )

        if source_id not in self.__edges:
            self.__edges[source_id] = set()

        self.__edges[source_id].add(Edge(source_id, target_id, weight))

    # def shortest_path_to_target(self, source_node_id, target_node_id):
    #
    # def shortest_path_to_all(self, source_node_id):
    #
    # def shortest_path_from_all_to_all(self):

    def is_cyclic(self):
        # edges =
        if self.__is_directed:
            directed_is_cyclic(self.__nodes, self.__weightless_edges)

        else:
            undirected_is_cyclic(self.__nodes, self.__weightless_edges)

    def minimum_spanning_tree(self):
        if not self.__is_directed:
            if self.__is_dense():
                return prim()
            else:
                flattened_edges =  utils.flatten(list(map(lambda node_id: list(self.__edges[node_id]), self.__edges)))

                return kruskal(self.__nodes, flattened_edges)
        else:
            return None

    def __is_dense(self):
        num_of_edges = len(utils.flatten(self.__weightless_edges()))

        return num_of_edges > len(self.__nodes)

    def __bfs(self, source_node_id):
        bfs(self.__weightless_edges, source_node_id)

    def __dfs(self, source_node_id):
        dfs(self.__weightless_edges, source_node_id)

    def __weightless_edges(self):
        weightless_edges = {}

        for node_id in self.__edges:
            weightless_edges[node_id] = set()

            for edge in self.__edges[node_id]:
                weightless_edges[node_id].add(edge.target)

        return weightless_edges








