import random


class _Heap[T]:
    """
    An implementation of a binary heap using an array. The sift up and sift down methods
    are implemented by child classes to exhibit the behavior of a Min Heap and Max Heap accordingly.

    Time Complexities:
        - Find max/min element: `O(1)`
        - Delete/remove max: `O(log n)`
        - Insert: `O(log n)`
    """
    def __init__(self, key: callable = lambda x: x[1]):
        self.key = key
        self.heap = []

    def __contains__(self, item):
        for value, _ in self.heap:
            if value == item:
                return True
        return False

    def __str__(self):
        return str(self.heap)

    # TODO: Add some sort of validation in case user tries to use values that cannot be compared
    # @staticmethod
    # def _validate(params: list[int]):
    #     def decorator(func):
    #         def wrapper(self, *args):
    #             self._validate_value([*args], params)
    #             return func(self, *args)
    #         return wrapper
    #     return decorator
    #
    # @staticmethod
    # def _validate_value(values, params_to_check):
    #     for pos in params_to_check:
    #         val = values[pos]
    #         raise TypeError('Parameter must be of type Comparable.') if not None and not isinstance(val, Comparable) else None

    def _sift_up(self, current_pos):
        raise NotImplementedError('Method must be overridden by child class.')

    def _sift_down(self, current_pos):
        raise NotImplementedError('Method must be overridden by child class.')

    @staticmethod
    def parent_pos(child_pos: int) -> int:
        return child_pos // 2

    @staticmethod
    def left_child_pos(parent_pos: int) -> int:
        return parent_pos * 2 + 1

    @staticmethod
    def right_child_pos(parent_pos: int) -> int:
        return parent_pos * 2 + 2

    def is_leaf(self, pos):
        return pos == self.size() or pos * 2 > self.size()

    def swap(self, child_pos: int, parent_pos: int):
        self.heap[child_pos], self.heap[parent_pos] = self.heap[parent_pos], self.heap[child_pos]

    def push(self, value: T, priority: int|float|str = None):
        self.heap.append((value, value if priority is None else priority))
        current_pos = self.size() - 1
        self._sift_up(current_pos)

    def pop(self) -> T:
        val = self.heap.pop(0)[0]
        if not self.is_empty():
            self.heap.insert(0, self.heap.pop())
        self._sift_down(0)
        return val

    def peek(self) -> T:
        return self.heap[0][0]

    def replace(self, value: T) -> T:
        old_val = self.heap.pop(0)
        self.heap[0] = value
        self._sift_down(0)
        return old_val

    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0


class MinHeap[T](_Heap):
    def __init__(self, key: callable = lambda x: x[1]):
        super().__init__(key=key)

    def _sift_up(self, current_pos):
        parent_pos = self.parent_pos(current_pos)

        while self.key(self.heap[current_pos]) < self.key(self.heap[parent_pos]):
            self.swap(current_pos, parent_pos)
            current_pos = self.parent_pos(current_pos)
            parent_pos = self.parent_pos(current_pos)

    def _sift_down(self, current_pos):
        if self.is_leaf(current_pos):
            return

        left_child_pos = self.left_child_pos(current_pos)
        right_child_pos = self.right_child_pos(current_pos)

        current_value = self.key(self.heap[current_pos])
        left_child_value = self.key(self.heap[left_child_pos]) if left_child_pos < self.size() else float('inf')
        right_child_value = self.key(self.heap[right_child_pos]) if right_child_pos < self.size() else float('inf')

        if current_value > left_child_value or current_value > right_child_value:
            # Swap with whichever child is smaller
            if left_child_value < right_child_value:
                self.swap(current_pos, left_child_pos)
                self._sift_down(left_child_pos)
            else:
                self.swap(current_pos, right_child_pos)
                self._sift_down(right_child_pos)


class MaxHeap[T](_Heap):
    def __init__(self, key: callable = lambda x: x[1]):
        super().__init__(key=key)

    def _sift_up(self, current_pos):
        parent_pos = self.parent_pos(current_pos)

        while self.key(self.heap[current_pos]) > self.key(self.heap[parent_pos]):
            self.swap(current_pos, parent_pos)
            current_pos = self.parent_pos(current_pos)
            parent_pos = self.parent_pos(current_pos)

    def _sift_down(self, current_pos):
        if self.is_leaf(current_pos):
            return

        left_child_pos = self.left_child_pos(current_pos)
        right_child_pos = self.right_child_pos(current_pos)

        current_value = self.key(self.heap[current_pos])
        left_child_value = self.key(self.heap[left_child_pos]) if left_child_pos < self.size() else float('-inf')
        right_child_value = self.key(self.heap[right_child_pos]) if right_child_pos < self.size() else float('-inf')

        if current_value < left_child_value or current_value < right_child_value:
            # Swap with whichever child is larger
            if left_child_value > right_child_value:
                self.swap(current_pos, left_child_pos)
                self._sift_down(left_child_pos)
            else:
                self.swap(current_pos, right_child_pos)
                self._sift_down(right_child_pos)


if __name__ == '__main__':
    minheap = MinHeap()
    print('Populating MinHeap with: ', end='')
    for i in range(10):
        random_int = random.randint(1, 100)
        print(str(random_int) + '... ', end='')
        minheap.push(random_int)
    print()

    print('Current MinHeap state: ', minheap)
    print('Popping from MinHeap... ', end='')
    for i in range(10):
        print(str(minheap.pop()) + '... ', end='')
    print()

    print()

    maxheap = MaxHeap()
    print('Populating MaxHeap with: ', end='')
    for i in range(10):
        random_int = random.randint(1, 100)
        print(str(random_int) + '... ', end='')
        maxheap.push(random_int)
    print()

    print('Current MaxHeap state: ', maxheap)
    print('Popping from MaxHeap... ', end='')
    for i in range(10):
        print(str(maxheap.pop()) + '... ', end='')
    print()

    minheap = MinHeap()
    minheap.push('A', 3)
    minheap.push('B', 1)
    minheap.push('C', 0)
    minheap.push('D', 2)
    print(minheap)
    minheap.update_value('D', 4)
    print(minheap)
    while not minheap.is_empty():
        print(minheap.pop())