from ds.hash_map import HashMap


class Graph[T]:
    """
    An optionally-directed, optionally-weighted graph implemented via a hash table representing an adjacency list.

    This implementation provides `O(1)` time for nearly all supported methods (amortized in some cases):
        - Add vertex
        - Add edge
        - Remove edge
        - Retrieve neighbors of node X
    The remaining operations have the following time complexities:
        - Check if nodes `x`, and `y` are adjacent: `O(e)` where `e` is the number of neighbors of `x`
        - Remove vertex: `O(v * e)` where `v` is the number of vertices in the graph and `e` is the average number
            of neighbors of each vertex
    """
    def __init__(self, directed=False):
        self._adjacency_list = HashMap()
        self._directed = directed

    def __contains__(self, item):
        return item in self._adjacency_list

    def __str__(self):
        return str(self._adjacency_list)

    @staticmethod
    def _validate(func):
        def wrapper(self, *args):
            self._validate_nodes([*args])
            return func(self, *args)
        return wrapper

    def _validate_nodes(self, nodes: [T]):
        for node in nodes[:2]:
            if node not in self._adjacency_list:
                raise KeyError(f'Value \'{node}\' not present in graph.')

    def add_vertex(self, value: T):
        if value not in self._adjacency_list:
            self._adjacency_list[value] = dict()

    @_validate
    def remove_vertex(self, value: T):
        del self._adjacency_list[value]

        for key in self._adjacency_list:
            if value in self._adjacency_list[key]:
                del self._adjacency_list[key][value]

    @_validate
    def add_edge(self, start: T, end: T, weight: int|None = None):
        """
        Add an edge from `start` to `end` with optional weight `weight`.

        Self-referential edges are disallowed.
        :param start: The source node of the edge. Must already be present in the graph.
        :param end: The sink node of the edge. Must already be present in the graph.
        :param weight: An integer value representing the weight of the edge.
        :return: None
        """
        # Disallow self-referential edges
        if start == end:
            return

        self._adjacency_list[start][end] = weight

        # Only add edge one way if graph is a directed graph
        if self._directed:
            return

        self._adjacency_list[end][start] = weight

    @_validate
    def remove_edge(self, start: T, end: T):
        del self._adjacency_list[start][end]

        if self._directed:
            return

        del self._adjacency_list[end][start]

    @_validate
    def neighbors(self, value: T) -> [(T, int)]:
        """
        Get all the neighbors (node, weight) of the node `value`.
        :param value: A value in the graph
        :return: A list of tuples representing the neighbors of `value` and the weights of their edges
        """
        return [(key, val) for key, val in self._adjacency_list[value].items()]

    @_validate
    def is_adjacent(self, first: T, second: T) -> bool:
        return second in self._adjacency_list[first]

    def nodes(self) -> [T]:
        return self._adjacency_list.keys()

    def edges(self) -> [(T, T, int)]:
        """
        Get all the edges of the graph along with their corresponding weights.

        Undirected graphs do not return duplicate edges. E.g. an edge from vertex 1 to vertex 2 with weight 5) will not
        return edges `(1, 2, 5)` and `(2, 1, 5)`, only the former.
        :return: A list of tuples `(v1, v2, weight)` representing the edges of the graph and their weights
        """
        edges = set()
        for node in self._adjacency_list:
            for neighbor in self.neighbors(node):
                edges.add((min(node, neighbor[0]), max(node, neighbor[0]), neighbor[1]))
        return list(edges)


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

    try:
        graph.add_edge(4, 6)
    except KeyError as e:
        print('Caught KeyError: ', e)

    print('Neighbors of node 2: ', str(graph.neighbors(2)))

    print('Is 2 adjacent to 3: ', str(graph.is_adjacent(2, 3)))

    print(graph)

    graph.remove_edge(2, 4)
    print('Remove edge 2-4:')
    print(graph)

    graph.remove_vertex(2)
    print('Remove 2:')
    print(graph)
