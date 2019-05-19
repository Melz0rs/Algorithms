from graph.prim import prim
from graph.kruskal import kruskal
from graph.bfs import bfs
from graph.dfs import dfs
import disjoint_sets.union_find as union_find
import utils

class Graph:

    nodes = set() # node ids
    edges = {} # from node id to set of node ids

    def __init__(self, is_directed):
        self.is_directed = is_directed

    def add_node(self, node_id):
        self.nodes.add(node_id)

    def add_edge(self, source_node_id, target_node_id, is_bidirectional=False):
        if source_node_id not in self.edges:
            self.edges[source_node_id] = set()

        self.edges[source_node_id].add(target_node_id)

        if is_bidirectional:
            self.add_edge(target_node_id, source_node_id)

    def union(self, parents, node_a, node_b):
        union_find.union(parents, node_a, node_b)

    def find_parent(self, parents, node):
        return union_find.find_parent(parents, node)


    def bfs(self, source_node_id):
        bfs(self.edges, source_node_id)

    def dfs(self, source_node_id):
        dfs(self.edges, source_node_id)

    def dijkstra(self):


    def floyd_warshall(self):


    def is_cyclic(self):
        if self.is_directed:
            # implement
        else:
            parents = {}

            for node_id in self.nodes:
                parents[node_id] = node_id

            for source_node_id in self.nodes:
                for target_node_id in self.edges[source_node_id]:
                    source_node_parent = union_find.find_parent(parents, source_node_id)
                    target_node_parent = union_find.find_parent(parents, target_node_id)

                    if source_node_parent == target_node_parent:
                        return True

                    union_find.union(parents, source_node_parent, target_node_parent)

            return False

    def minimum_spanning_tree(self):
        if self.is_dense():
            return prim()
        else:
            return kruskal()


    def is_dense(self):
        num_of_edges = len(utils.flatten(self.edges))

        return num_of_edges > len(self.nodes)






