from ds.hash_map import HashMap


class Graph[T]:
    """
    An undirected graph implemented via a hash table representing an adjacency list.

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

    def __str__(self):
        return str(self._adjacency_list)

    @staticmethod
    def _validate(func):
        def wrapper(self, *args):
            self._validate_nodes([*args])
            return func(self, *args)
        return wrapper

    def _validate_nodes(self, nodes: [T]):
        for node in nodes:
            if node not in self._adjacency_list:
                raise KeyError(f'Value \'{node}\' not present in graph.')

    def add_vertex(self, value: T):
        if value not in self._adjacency_list:
            self._adjacency_list[value] = set()

    @_validate
    def remove_vertex(self, value: T):
        del self._adjacency_list[value]

        for key in self._adjacency_list:
            if value in self._adjacency_list[key]:
                self._adjacency_list[key].remove(value)

    @_validate
    def add_edge(self, start: T, end: T):
        # Disallow self-referential edges
        if start == end:
            return

        self._adjacency_list[start].add(end)

        # Only add edge one way if graph is a directed graph
        if self._directed:
            return

        self._adjacency_list[end].add(start)

    @_validate
    def remove_edge(self, start: T, end: T):
        self._adjacency_list[start].remove(end)

        if self._directed:
            return

        self._adjacency_list[end].remove(start)

    @_validate
    def neighbors(self, value: T) -> [T]:
        return self._adjacency_list[value]

    @_validate
    def adjacent(self, first: T, second: T) -> bool:
        return second in self.neighbors(first)

    def nodes(self) -> [T]:
        return self._adjacency_list.keys()


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

    print('Is 2 adjacent to 3: ', str(graph.adjacent(2, 3)))

    print(graph)

    graph.remove_edge(2, 4)
    print('Remove edge 2-4:')
    print(graph)

    graph.remove_vertex(2)
    print('Remove 2:')
    print(graph)
