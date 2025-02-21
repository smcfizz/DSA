from ds.hash_map import HashMap


class DisjointSet[T]:
    """
    Disjoint set data structure utilizing union by rank and path compression optimizations

    With the above-mentioned optimizations, find() and union() have a runtime of O(a(n))
    where a(n) is the inverse Ackermann function. For practical purposes, we can treat this O(1)
    """
    def __init__(self):
        self._parent = HashMap()
        self._rank = HashMap()

    def make_set(self, nums: list[T]):
        for n in nums:
            self._parent[n] = n
            self._rank[n] = 0

    def find(self, n: T):
        if n not in self._parent:
            return None
        if self._parent[n] != n:
            # path compression, flatten the tree by raising all nodes to the root
            self._parent[n] = self.find(self._parent[n])
        return self._parent[n]

    def union(self, n1: T, n2: T):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return
        # union by rank, merge trees with lower rank into the tree with higher rank
        # to prevent tree growth and improve performance of find() by keeping trees small
        if self._rank[p1] > self._rank[p2]:
            self._parent[p2] = p1
        elif self._rank[p1] < self._rank[p2]:
            self._parent[p1] = p2
        else:
            self._parent[p2] = p1
            self._rank[p1] += 1


if __name__ == '__main__':
    universe = [1, 2, 3, 4, 5]
    ds = DisjointSet()
    ds.make_set(universe)
    print([ds.find(i) for i in universe])
    ds.union(1, 2)
    print([ds.find(i) for i in universe])
    ds.union(2, 3)
    print([ds.find(i) for i in universe])
    ds.union(3, 4)
    print([ds.find(i) for i in universe])
    ds.union(4, 5)
    print([ds.find(i) for i in universe])