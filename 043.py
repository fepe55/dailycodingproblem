"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Implement a stack that has the following methods:

- push(val), which pushes an element onto the stack
- pop(), which pops off and returns the topmost element of the stack.
If there are no elements in the stack, then it should throw an error or return
null.
- max(), which returns the maximum value in the stack currently.
If there are no elements in the stack, then it should throw an error or return
null.

Each method should run in constant time.
"""


class Stack:
    def __init__(self):
        self._stack = []
        self._max_stack = []

    def push(self, val):
        self._stack.append(val)
        if not self._max_stack or val > self._max_stack[-1]:
            self._max_stack.append(val)
        return val

    def pop(self):
        if not self._stack:
            return None
        last_elem = self._stack.pop()
        if last_elem == self._max_stack[-1]:
            self._max_stack.pop()
        return last_elem

    def max(self):
        if not self._max_stack:
            return None
        return self._max_stack[-1]


if __name__ == '__main__':
    stack = Stack()
    assert not stack.pop()
    assert not stack.max()
    stack.push(2)
    assert stack.max() == 2
    stack.push(3)
    assert stack.max() == 3
    stack.push(1)
    assert stack.max() == 3
    assert stack.pop() == 1
    assert stack.max() == 3
    assert stack.pop() == 3
    assert stack.max() == 2
    assert stack.pop() == 2
    assert not stack.pop()
    assert not stack.max()
