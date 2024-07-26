from typing import Any, Optional


class _LinkedListNode:
    """
    A node in a linked list.
    """
    def __init__(self, data: Any, next: Optional['_LinkedListNode'] = None, prev: Optional['_LinkedListNode'] = None) -> None:
        """
        Initialize a _Node object.

        Args:
            data (Any): The data to be stored in the _Node.
            next (Optional['_Node']): The next _Node in the linked list. Defaults to None.
            prev (Optional['_Node']): The previous _Node in the linked list. Defaults to None.
        """
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return '[ ' + str(self.data) + ' ]'


class LinkedList[T]:
    """
    A doubly linked list with generic type support.
    """
    def __init__(self, data: T = None):
        if data:
            self.head = _LinkedListNode(data)
            self.tail = self.head
        else:
            self.head = None
            self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __reversed__(self):
        node = self.tail
        while node:
            yield node
            node = node.prev

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def __str__(self):
        if self.head is None:
            return '( Empty )'
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node))
            node = node.next
        return " <-> ".join(nodes)

    def add(self, data: T):
        """
        Add a node to the end of the list.
        :param data:
        :return:
        """
        if self.head is None:
            self.head = _LinkedListNode(data, None, None)
            self.tail = self.head
        else:
            self.tail.next = _LinkedListNode(data, None, self.tail)
            self.tail = self.tail.next

    def insert_at[int](self, data: T, index: int = 0):
        """
        Insert a node at the given index.
        :param data: The value to insert into the list.
        :param index: The index of the position in the list to insert the new node.
            Defaults to 0. A value of -1 inserts at the end.
        :raises IndexError: If the index is less than -1 or greater than the length of the list.
        """
        if -1 > index > len(self):
            raise IndexError('Index out of range')
        if index == -1:
            self.tail.next = _LinkedListNode(data, None, self.tail)
            self.tail = self.tail.next
            return
        if index == 0:
            self.head = _LinkedListNode(data, self.head)
            return
        count = 0
        node = self.head
        while node:
            if count == index - 1:
                temp = node.next
                node.next = _LinkedListNode(data, node.next, node)
                node.next.prev = node
                node.next.next = temp
                temp.prev = node.next
                return
            count += 1
            node = node.next

    def find(self, data: T) -> Optional['_LinkedListNode']:
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    def remove_at(self, index: int = 0):
        """
        Remove the node at the given index.
        :param index: The index of the node to remove. Defaults to 0. A value of -1 removes the last node.
        :raises IndexError: If the index is less than -1 or greater than or equal to the length of the list.
        """
        if len(self) == 0:
            raise IndexError('List is empty')
        if -1 > index >= len(self):
            raise IndexError('Index out of range')
        if index == -1:
            val = self.tail.data
            if len(self) == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            return val
        if index == 0:
            val = self.head.data
            self.head = self.head.next
            return val
        count = 0
        node = self.head
        while node:
            if count == index - 1:
                val = node.next.data
                node.next = node.next.next
                node.next.prev = node
                return val
            count += 1
            node = node.next


if __name__ == "__main__":
    # Construct a linked list:
    linked_list = LinkedList[int]()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)

    # Add a value of a differing type (linter warnings are shown):
    linked_list.add('a')

    # Print the linked list:
    print(linked_list)

    # Insert 4 at index 1:
    linked_list.insert_at(4, 1)
    print(linked_list)

    # Find 3 in the linked list:
    node = linked_list.find(3)
    print(node)

    # Get the length of the linked list:
    print('Length: ', len(linked_list))

    # Iterate over the linked list and perform operations:
    print([node.data * 2 for node in linked_list])

    # Remove the last node:
    linked_list.remove_at(-1)
    print(linked_list)

    # Iterate in reverse:
    print(' -> '.join([str(node) for node in reversed(linked_list)]))
