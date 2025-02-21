from ds.graph import Graph
from ds.disjoint_set import DisjointSet

def union_find(graph: Graph[int]) -> bool:
    """
    Determine if a graph contains a cycle using the Union-Find algorithm.

    Time complexity: O(E) where E is the number of edges in the graph
        - (Technically O(E * α(n)) where α(n) is the inverse Ackermann function, but we can treat this as a constant)
    Space complexity: O(V) where V is the number of vertices in the graph

    union() and find() have a runtime of O(a(n)) where a(n) is the inverse Ackermann function.
    For practical purposes, we can treat this as a constant (see DisjointSet implementation).
    """
    ds = DisjointSet()
    ds.make_set(graph.nodes())

    for v1, v2, _ in graph.edges():
        if ds.find(v1) == ds.find(v2):
            return True
        ds.union(v1, v2)

    return False


if __name__ == '__main__':
    graph = Graph[int]()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)

    if union_find(graph):
        print('Graph contains a cycle.')
    else:
        print('Graph does not contain a cycle.')