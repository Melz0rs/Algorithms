from graph.prim import prim
from graph.kruskal import kruskal
from graph.bfs import bfs
from graph.dfs import dfs
import disjoint_sets.union_find as union_find
import utils

class Graph:

    __nodes = set() # node ids
    __edges = {} # from node id to set of node ids

    def __init__(self, is_directed):
        self.__is_directed = is_directed

    def add_node(self, node_id):
        self.__nodes.add(node_id)

    def add_edge(self, source_node_id, target_node_id, is_bidirectional=False):
        if source_node_id not in self.__edges:
            self.__edges[source_node_id] = set()

        self.__edges[source_node_id].add(target_node_id)

        if is_bidirectional:
            self.add_edge(target_node_id, source_node_id)



    def dijkstra(self):


    def floyd_warshall(self):


    def is_cyclic(self):
        if self.__is_directed:
            self.__is_cyclic_directed()

        else:
            self.__is_cyclic_undirected()



    def minimum_spanning_tree(self):
        if self.__is_dense():
            return prim()
        else:
            return kruskal()


    def __is_cyclic_undirected(self):
        parents = {}

        for node_id in self.__nodes:
            parents[node_id] = node_id

        for source_node_id in self.__nodes:
            for target_node_id in self.__edges[source_node_id]:
                source_node_parent = union_find.find_parent(parents, source_node_id)
                target_node_parent = union_find.find_parent(parents, target_node_id)

                if source_node_parent == target_node_parent:
                    return True

                union_find.union(parents, source_node_parent, target_node_parent)

        return False


    def __is_cyclic_directed(self):

        def has_already_visited(node_id, visited):
            return node_id in visited

        random_node = next(iter(self.__nodes))
        is_cyclic = False

        dfs(self.__edges, random_node, visit_fn=has_already_visited)

        return is_cyclic


    def __is_dense(self):
        num_of_edges = len(utils.flatten(self.__edges))

        return num_of_edges > len(self.__nodes)


    def __bfs(self, source_node_id):
        bfs(self.__edges, source_node_id)


    def __dfs(self, source_node_id):
        dfs(self.__edges, source_node_id)







