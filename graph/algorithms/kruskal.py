from common.sorts.merge_sort import merge_sort
from graph.undirected.is_cyclic import is_cyclic


def kruskal(nodes, edges):
    included_edges = []
    edges = edges.copy()
    merge_sort(edges, __is_smaller)
    edge_index = 0

    while len(included_edges) < len(nodes) - 1:
        next_edge = edges[edge_index]
        edge_index += 1

        included_edges.append(next_edge)

        is_cycle_formed = is_cyclic(nodes, __weightless_edges(included_edges))

        if is_cycle_formed:
            included_edges.pop()

    # included_edges_formatted = list(map(lambda edge: {edge.source: edge.target}, included_edges))

    return included_edges


def __is_smaller(edge1, edge2):
    return edge1.weight < edge2.weight


def __weightless_edges(edges):
    weightless_edges = {}

    for edge in edges:
        if edge.source not in weightless_edges:
            weightless_edges[edge.source] = set()

        weightless_edges[edge.source].add(edge.target)

    return weightless_edges

