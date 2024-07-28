from typing import Any, Optional

from my_queue import ArrayQueue as Queue


class NotFoundException(Exception):
    pass


class _TreeNode:
    class _Child:
        LEFT = 0
        RIGHT = 1

    def __init__(self, val: Any, left: Optional['_TreeNode'] | None = None, right: Optional['_TreeNode'] = None):
        self.val = val
        self.count = 1  # To handle duplicates
        self.left = left
        self.right = right

    def __str__(self):
        return f'[ {str(self.val)} ]'

    def insert(self, new_node: '_TreeNode'):
        if new_node.val == self.val:
            self.count += 1
            return
        if new_node.val > self.val:
            if self.right is None:
                self.right = new_node
                return
            self.right.insert(new_node)
        if new_node.val < self.val:
            if self.left is None:
                self.left = new_node
                return
            self.left.insert(new_node)

    def remove(self, target: Any):
        if target < self.val:
            if self.left.val == target:
                target_node = self.left
                self.left = target_node.right
                self.left.insert(target_node.left)
                return
            return self.left.remove(target)
        if target > self.val:
            if self.right.val == target:
                target_node = self.right
                self.right = target_node.right
                self.right.insert(target_node.left)
                return
            return self.right.remove(target)

    def find(self, val: Any) -> bool:
        if val == self.val:
            return True
        if val < self.val and self.left is not None:
            return self.left.find(val)
        if val > self.val and self.right is not None:
            return self.right.find(val)
        return False


class BinarySearchTree[T]:
    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self._level_order())

    def _level_order(self) -> [T]:
        if self.is_empty():
            return []

        vals = []
        q = Queue[_TreeNode]()

        q.enqueue(self.head)
        while not q.is_empty():
            node = q.dequeue()
            vals.append(node.val)

            left = node.left
            if left is not None:
                q.enqueue(left)

            right = node.right
            if right is not None:
                q.enqueue(right)

        return vals

    def is_empty(self):
        return self.head is None

    def insert(self, val: T):
        if self.head is None:
            self.head = _TreeNode(val)
            return

        self.head.insert(_TreeNode(val))

    def remove(self, target: T):
        if not self.find(target):
            raise NotFoundException({'message': 'Element not present in tree.', 'element': str(target)})

        if target == self.head.val:
            if self.head.count > 1:
                self.head.count -= 1
                return

            if self.head.right is None:
                self.head = self.head.left
                return

            new_head = self.head.right
            if self.head.left is not None:
                new_head.insert(self.head.left)
                self.head = new_head
                return

        self.head.remove(target)

    def find(self, target: T) -> bool:
        if self.head is None:
            return False
        return self.head.find(target)


if __name__ == '__main__':
    # Initialize a new tree
    bst = BinarySearchTree[int]()
    bst.insert(10)
    bst.insert(30)
    bst.insert(5)
    bst.insert(1)
    bst.insert(40)
    bst.insert(20)
    bst.insert(15)
    bst.insert(25)
    bst.insert(23)
    bst.insert(28)
    bst.insert(17)
    bst.insert(11)
    print('Print in level order:', bst)

    # Search for values
    print('Found 10: ', bst.find(10))
    print('Found 4: ', bst.find(4))
    print('Found 5: ', bst.find(5))

    # Remove values
    bst.remove(20)
    print('Removed 20')
    print(bst)

    try:
        bst.remove(100)
    except NotFoundException as e:
        print('Caught NotFoundException: ', e)
