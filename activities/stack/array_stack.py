""""Implement a stack collection that supports `is_empty`, `push` and `pop`."""

class ArrayStack:

    def __init__(self):
        self._data = [None]
        self._size = 0


    def push(self, item):
        if self._size == len(self._data):
            self._expand()
        self._data[self._size] = item
        self._size += 1

    def pop(self):
        self._size -= 1
        return self._data[self._size]

    def is_empty(self):
        return self._size == 0
    
    def _expand(self):
        n = len(self._data)
        new_data = [None] * n * 2
        for i in range(n - 1):
            new_data[i] = self._data[(self._front + i) % n]
        self._front = 0
        self._back = n - 1
        self._data = new_data
