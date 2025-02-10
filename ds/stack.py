import os

from linked_list import LinkedList


class LinkedListStack[T]:
    """
    A stack implemented with a linked list.

    Here I am simply reusing the LinkedList I have already implemented.
    """
    def __init__(self):
        self.stack = LinkedList[T]()

    def push(self, data: T):
        self.stack.add(data)

    def pop(self) -> T:
        return self.stack.remove_at(-1)

    def __str__(self):
        return str(self.stack)


class ArrayStack[T]:
    """
    A stack implemented with an array.

    Since this is Python, we will be ignoring the special functionality of the list
    to simulate the immutability of arrays as they exist in other languages like C.
    """
    def __init__(self):
        """
        We keep track of the top of the stack using a pointer. This allows us to avoid copying the stack data into a
        new array each time we push data and results in O(1) amortized time for both push and pop operations. Space
        complexity is O(n) where n is the size of the stack.
        """
        self.stack = []  # size of 0
        self.top = 0  # index of the top of the stack (first available space)

    def push(self, data: T):
        if self.top == len(self.stack):
            # Initialize a new array that is twice as large
            new_length = len(self.stack) * 2 if len(self.stack) > 0 else 1
            new_stack = [None] * new_length

            # Copy the old array into the new one and add the new data
            for i in range(len(self.stack)):
                new_stack[i] = self.stack[i]

            # Update the stack
            self.stack = new_stack

        self.stack[self.top] = data
        self.top += 1

    def pop(self) -> T:
        if (self.top - 1) < 0:
            raise IndexError('Stack is empty')
        self.top -= 1
        val = self.stack[self.top]
        self.stack[self.top] = None  # We don't have to clear old data, but I do anyway
        return val

    def __str__(self):
        return f"{str(self.stack)}{os.linesep}top: {self.top}"


if __name__ == '__main__':
    print('---- Test Stack with Linked List -----')
    # Initialize and populate the stack
    llstack = LinkedListStack[int]()
    llstack.push(1)
    llstack.push(2)
    llstack.push(3)
    print(llstack)

    # Pop from the stack
    print('Popped: ', llstack.pop())
    print('Popped: ', llstack.pop())
    print('Popped: ', llstack.pop())
    print(llstack)

    # Pop from an empty stack
    try:
        print('Popped: ', llstack.pop())
    except IndexError as e:
        print('Caught IndexError: ', e)
    print()

    print('---- Test Stack with Array -----')
    # Initialize and populate the stack
    arrstack = ArrayStack[int]()
    arrstack.push(1)
    arrstack.push(2)
    arrstack.push(3)
    print(arrstack)

    # Pop from the stack
    print('Popped: ', arrstack.pop())
    print('Popped: ', arrstack.pop())
    print('Popped: ', arrstack.pop())
    print(arrstack)

    # Pop from an empty stack
    try:
        print('Popped: ', arrstack.pop())
    except IndexError:
        print('Caught IndexError: Stack is empty')
