from linked_list import LinkedList


class LinkedListQueue[T]:
    """
    A queue implemented with a linked list.

    Maybe it's somewhat cheating, but I already
    implemented a LinkedList, so I'm going to use it here.
    """
    def __init__(self):
        self.queue = LinkedList[T]()

    def enqueue(self, data: T):
        self.queue.insert_at(data, 0)

    def dequeue(self) -> T:
        return self.queue.remove_at(0)

    def __str__(self):
        return str(self.queue)


class ArrayQueue[T]:
    """
    A queue implemented with an array.

    As with our Stack implementation, we will be ignoring the build-in functionality of Python's list
    in order to properly address the technical challenges of implementing a queue.
    """
    def __init__(self):
        """
        Also in similar fashion to our Stack implementation, we will use a pointer to keep track of the
        front of our queue in order to amortize our time complexity to O(1) for enqueues and dequeues.
        Space complexity is O(n) where n is the size of the queue.
        """
        self.queue = []
        self.front = 0
        self.back = 0
        self.size = 0

    def _reset_pointers(self):
        self.front = 0
        self.back = 0

    def _resize_queue(self):
        new_length = len(self.queue) * 2 if len(self.queue) > 0 else 1
        new_queue = [None] * new_length
        for i, n in enumerate(self.queue):
            new_queue[i] = n
        self.queue = new_queue

    def _shift_to_front(self):
        for old_position in range(self.front, self.back):
            new_position = old_position - self.front
            self.queue[new_position] = self.queue[old_position]
            self.queue[old_position] = None

        self.back -= self.front
        self.front = 0

    def _clean_queue(self):
        """
        Shift all values in queue forward to the front of the internal array
        to ensure space is being used efficiently, then expand the queue if necessary.
        :return:
        """
        if self.front != 0:
            self._shift_to_front()
        if self.size == len(self.queue):
            self._resize_queue()

    def enqueue(self, data: T):
        self._clean_queue()
        self.queue[self.back] = data
        self.back += 1
        self.size += 1

    def dequeue(self) -> T:
        if (self.back - 1) < 0 or self.front == self.back:
            self._reset_pointers()
            raise IndexError('Queue is empty')

        val = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        self.size -= 1
        return val

    def is_empty(self) -> bool:
        return self.size == 0

    def peek(self) -> T | None:
        if self.is_empty():
            return None
        return self.queue[self.back - 1]

    def size(self) -> int:
        return self.size

    def __str__(self):
        return f'{str(self.queue)}\nfront: {self.front}, back: {self.back}'


if __name__ == '__main__':
    print('---- Test Queue with Linked List -----')
    # Initialize and populate the queue
    llqueue = LinkedListQueue[int]()
    llqueue.enqueue(1)
    llqueue.enqueue(2)
    llqueue.enqueue(3)
    print(llqueue)

    # Pop from the queue
    print('Popped: ', llqueue.dequeue())
    print('Popped: ', llqueue.dequeue())
    print('Popped: ', llqueue.dequeue())
    print(llqueue)

    # Pop from an empty queue
    try:
        print('Popped: ', llqueue.dequeue())
    except IndexError as e:
        print('Caught IndexError: ', e)
    print()

    print('---- Test Queue with Array -----')
    # Initialize and populate the queue
    arrqueue = ArrayQueue[int]()
    arrqueue.enqueue(1)
    arrqueue.enqueue(2)
    arrqueue.enqueue(3)
    arrqueue.enqueue(4)
    arrqueue.enqueue(5)
    print(arrqueue)

    # Pop from the queue
    print('Popped: ', arrqueue.dequeue())
    print('Popped: ', arrqueue.dequeue())
    print('Popped: ', arrqueue.dequeue())
    print(arrqueue)
    arrqueue.enqueue(6)
    print(arrqueue)
    print('Popped: ', arrqueue.dequeue())
    print('Popped: ', arrqueue.dequeue())
    print('Popped: ', arrqueue.dequeue())

    # Pop from an empty queue
    try:
        print('Popped: ', arrqueue.dequeue())
    except IndexError as e:
        print('Caught IndexError: ', e)
