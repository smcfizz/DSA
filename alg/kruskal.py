from ds.graph import Graph
from alg.union_find import union_find

def kruskal(graph: Graph[int]) -> Graph[int]:
    """
    Kruskal's algorithm for finding the minimum spanning tree of a graph.

    Time complexity: O(E log E) where E is the number of edges in the graph.
    Time complexity is dominated by the sorting of edges.
        - (Technically O(E log E + E^2 * α(n)) where α(n) is the inverse Ackermann function,
          but since the inverse Ackermann function grows very slowly, we can drop this term for practical purposes)
    Space complexity: O(V + E) where V is the number of vertices in the graph and E is the number of edges.
    """
    mst = Graph[int](directed= False)
    edges = graph.edges()
    edges.sort(key=lambda edge: edge[2]) # Sort edges by weight

    # add vertices to mst
    for v in graph.nodes():
        mst.add_vertex(v)

    # add edges to mst
    for edge in edges:
        mst.add_edge(edge[0], edge[1], edge[2])
        if not union_find(mst):
            if len(mst.edges()) == len(graph.nodes()) - 1:
                return mst
            continue
        mst.remove_edge(edge[0], edge[1])

    return mst


if __name__ == '__main__':
    graph = Graph[int](directed= False)
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_edge(0, 1, 7)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 3, 9)
    graph.add_edge(1, 4, 7)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 15)
    graph.add_edge(3, 5, 6)
    graph.add_edge(4, 5, 8)
    graph.add_edge(4, 6, 9)
    graph.add_edge(5, 6, 11)
    # Image of graph at:
    # https://i0.wp.com/www.techiedelight.com/wp-content/uploads/2016/11/Kruskal-1.png?resize=467%2C300&ssl=1

    print(kruskal(graph))