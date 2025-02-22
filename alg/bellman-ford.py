from typing import Any

from ds.graph import Graph


def bellman_ford(graph: Graph, start) -> (dict[Any, int], dict[Any, Any]):
    """
    Bellman-Ford Algorithm used to find the shortest path between two nodes
    in a weighted graph where there may be negative weights.

    Time complexity: O(E * V) where E is the number of edges in the graph and V is the number of vertices.
    Space complexity: O(V)
    """
    if start not in graph:
        raise KeyError(f'Value \'{start}\' not present in graph.')

    distances = {start: 0}
    predecessors = {start: None}
    for v in graph.nodes():
        if v != start:
            distances[v] = float('inf')
            predecessors[v] = None

    for _ in range(len(graph.nodes()) - 1):
        for u, v, w in graph.edges():
            alt = distances[u] + w
            if alt < distances[v]:
                distances[v] = alt
                predecessors[v] = u

    for u, v, w in graph.edges():
        alt = distances[u] + w
        if alt < distances[v]:
            raise ValueError('Graph contains a negative cycle')

    return distances, predecessors


if __name__ == '__main__':
    graph = Graph[str](directed= True)
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_edge('A', 'B', -1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 3)
    graph.add_edge('B', 'D', 2)
    graph.add_edge('B', 'E', 2)
    graph.add_edge('D', 'C', 5)
    graph.add_edge('D', 'B', 1)
    graph.add_edge('E', 'D', -3)

    dist, pred = bellman_ford(graph, 'A')
    print('Distances from A: ', dist)
    print('Predecessors: ', pred)