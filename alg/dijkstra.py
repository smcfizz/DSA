from typing import Any

from ds.graph import Graph
from ds.heap import MinHeap


def dijkstra(graph: Graph, start: str) -> (dict[Any, int], dict[Any, str]):
    """
    Dijkstra's Algorithm used to find the shortest path between two nodes in a weighted graph.

    Time complexity: O(E log V) where E is the number of edges in the graph and V is the number of vertices.
    Space complexity: O(E + V)
    """
    if start not in graph:
        raise KeyError(f'Value \'{start}\' not present in graph.')

    distances = {start: 0}
    predecessors = {start: None}
    queue = MinHeap()

    for v in graph.nodes():
        if v != start:
            distances[v] = float('inf')
            predecessors[v] = None

        queue.push(v, distances[v])

    while not queue.is_empty():
        u = queue.pop()[0]
        for v, w in graph.neighbors(u):
            alt = distances[u] + w
            if v in queue and alt < distances[v]:
                distances[v] = alt
                predecessors[v] = u
                queue.update_value(v, distances[v])

    return distances, predecessors


if __name__ == '__main__':
    graph = Graph[str](directed= True)
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_edge('A', 'B', 10)
    graph.add_edge('A', 'E', 3)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'E', 4)
    graph.add_edge('C', 'D', 9)
    graph.add_edge('D', 'C', 7)
    graph.add_edge('E', 'D', 2)
    graph.add_edge('E', 'B', 1)
    graph.add_edge('E', 'C', 8)
    # image of graph:
    # https://i0.wp.com/www.techiedelight.com/wp-content/uploads/2016/11/Dijkstras-7.png?resize=548%2C387&ssl=1

    dist, pred = dijkstra(graph, 'A')
    print('Distances from A: ', dist)
    print('Predecessors: ', pred)