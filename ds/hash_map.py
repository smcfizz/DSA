from typing import Any, Tuple


class HashMap:
    """
    An implementation of a HashMap using Open Addressing and linear probing to cache values and address collisions.
    I chose to use open addressing over separate chaining due to the lower amount of average cache misses per lookup
    and made a point to keep track of the load factor and rehash the array any time it increased above 75%.

    Alternatively, we could use a Linked List instead of an array to implement the hash map via Separate Chaining.
    """
    def __init__(self):
        self.map: [Tuple[Any, Any] | None] = [None]
        self.num_entries = 0

    def __contains__(self, key) -> bool:
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False

    def __iter__(self):
        for i in self.map:
            if i is not None:
                yield i[0]
            else:
                continue

    def __getitem__(self, key):
        hash_val = self._hash(key)

        while self.map[hash_val] is not None:
            if self.map[hash_val][0] == key:
                return self.map[hash_val][1]
            hash_val += 1

        raise KeyError(str(key))

    def __setitem__(self, key, value, rehash=True):
        hash_val: int = self._hash(key)

        # Handle overwrites first
        if self.map[hash_val] is not None and self.map[hash_val][0] == key:
            self.map[hash_val] = (key, value)
            return

        # For collisions, look for next open spot in array (linear probing)
        while self.map[hash_val] is not None:
            new_pos = hash_val + 1
            hash_val = new_pos if new_pos < len(self.map) else 0

        self.map[hash_val] = (key, value)
        self.num_entries += 1

        if rehash:
            self._rehash()

    def __delitem__(self, key):
        hash_val = self._hash(key)

        while self.map[hash_val] is not None:
            if self.map[hash_val][0] == key:
                self.map[hash_val] = None
                self.num_entries -= 1
                self._rehash()
                return
            hash_val += 1

    def _rehash(self):
        def transfer_map(old_map):
            for value in old_map:
                if value is not None:
                    self.__setitem__(value[0], value[1], rehash=False)
            self._rehash()

        if self._load_factor > 0.75:
            old_map = self.map
            self.map = [None] * len(self.map) * 2
            self.num_entries = 0
            transfer_map(old_map)
            return

        if self._load_factor < 0.25:
            if self._load_factor == 0 and len(self.map) == 1:
                return
            old_map = self.map
            self.map = [None] * int(len(self.map) / 2)
            self.num_entries = 0
            transfer_map(old_map)
            return

    def _hash(self, key) -> int:
        return hash(key) % len(self.map)

    @property
    def _load_factor(self) -> float:
        return self.num_entries / len(self.map) if self.num_entries > 0 else 0

    def __str__(self):
        return '\n'.join([f'{v[0]}\t|\t{v[1]}' for v in self.map if v is not None]) + '\n'


if __name__ == '__main__':
    # Construct a hash map
    hmap = HashMap()
    print('HashMap:\n', hmap)

    # Insert some values
    hmap['a'] = 123
    hmap[6512] = 'fizzbuzz'
    hmap[('apple', 'orange', 'banana')] = {'jane': 1234567, 'john': 9876543}
    print('HashMap:\n', hmap)

    print('True' if 'a' in hmap else 'False')
    print(hmap['a'])
    try:
        print(hmap['d'])
    except KeyError as e:
        print(f'No key {e} in map')
    print()

    # Overwrite a value
    hmap['a'] = 'Hello world'
    print('HashMap:\n', hmap)

    # Delete some values (notice the rehash to reduce internal array size and conserve memory)
    del hmap[('apple', 'orange', 'banana')]
    del hmap[6512]
    del hmap['a']
    print('HashMap:\n', hmap)
