class Trie[str]:
    """
    A Trie, offering `O(n * m)` time for search, insert, and delete operations where `n` is
    the size of the parameter and `m` is the size of the alphabet.

    In this example, the trie supports strings comprised of any ASCII character.
    """
    def __init__(self):
        self.children: [Trie | None] = [None] * 256
        self.value: str = None
        self.is_leaf: bool = False

    def insert(self, value: str):
        node = self
        for c in value:
            if node.children[ord(c)] is None:
                node.children[ord(c)] = Trie()
            node = node.children[ord(c)]
        node.value = value
        node.is_leaf = True

    def remove(self, value: str):
        def rem(node: 'Trie', value: str):
            if len(value) == 0:
                if node.is_leaf:
                    node.is_leaf = False
                    node.value = None
                for i in range(len(node.children)):
                    if node.children[i] is not None:
                        return node
                return None
            node.children[ord(value[0])] = rem(node.children[ord(value[0])], value[1:])
            return node

        rem(self, value)

    def contains(self, value: str) -> bool:
        node = self
        for c in value:
            if node.children[ord(c)] is None:
                return False
            node = node.children[ord(c)]
        return node.value is not None


if __name__ == '__main__':
    trie = Trie()
    trie.insert('h')
    trie.insert('hello')
    trie.insert('help')
    trie.insert('happy')

    print(trie.contains('hello'))
    print(trie.contains('hell'))
    print(trie.contains('goodbye'))

    trie.remove('hello')

    print(trie.contains('hello'))
    print(trie.contains('hell'))
    print(trie.contains('help'))
    print(trie.contains('h'))
    print(trie.contains('goodbye'))
