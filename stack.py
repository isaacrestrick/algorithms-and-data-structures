class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def __len__(self):
        return len(self._data)

    def empty(self):
        return len(self._data) == 0


class MinStack:
    """Stack supporting O(1) min retrieval."""

    def __init__(self):
        self._stack = []
        self._mins = []

    def push(self, x):
        self._stack.append(x)
        if not self._mins:
            self._mins.append(x)
        else:
            self._mins.append(x if x < self._mins[-1] else self._mins[-1])

    def pop(self):
        if not self._stack:
            raise IndexError("pop from empty stack")
        self._mins.pop()
        return self._stack.pop()

    def peek(self):
        if not self._stack:
            raise IndexError("peek from empty stack")
        return self._stack[-1]

    def get_min(self):
        if not self._mins:
            raise IndexError("min from empty stack")
        return self._mins[-1]

    def __len__(self):
        return len(self._stack)

    def empty(self):
        return len(self._stack) == 0


if __name__ == "__main__":
    s = Stack()
    assert s.empty()
    s.push(1)
    s.push(2)
    assert len(s) == 2
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.empty()

    m = MinStack()
    m.push(3)
    assert m.get_min() == 3
    m.push(1)
    assert m.get_min() == 1
    m.push(2)
    assert m.get_min() == 1
    assert m.pop() == 2
    assert m.get_min() == 1
    assert m.pop() == 1
    assert m.get_min() == 3
