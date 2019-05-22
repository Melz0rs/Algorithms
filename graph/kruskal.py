from common.sorts.merge_sort import merge_sort

def kruskal(nodes, edges, included_edges=None):
    if included_edges is None:
        included_edges = set()

    merge_sort(edges)

    while len(included_edges) < len(nodes):
