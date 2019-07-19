import stdio
import sys


class Deque:

    def __init__(self):
        self._first = None
        self._last = None
        self._n = 0

    def isEmpty(self):
        return self._n == 0

    def enqueue(self, item):
        oldLast = self._last
        self._last = _Node(item, None, self._last)
        if self.isEmpty():
            self._first = self._last
        else:
            oldLast.next = self._last
        self._n += 1

    def dequeue(self):
        item = self._last.item
        if self.isEmpty():
            self._last = None
        self._n -= 1
        return item

    def push(self, item):
        self._first = _Node(item, self._first, None)
        self._n += 1

    def pop(self):
        item = self._first.item
        self._first = self._first.next
        self._n -= 1
        return item

    def __str__(self):
        s = ''
        cur = self._first
        while cur is not None:
            s += str(cur.item) + ' '
            cur = cur.next
        return s


class _Node:
    def __init__(self, item, next, prev):
        self.item = item
        self.next = next
        self.prev = prev


def main():
    deque = Deque()
    stdio.writeln(deque.isEmpty())
    for i in range(1, 4):
        deque.enqueue(int(sys.argv[i]))
    for i in range(4, 7):
        deque.push(int(sys.argv[i]))
    deque.enqueue(7)
    deque.push(8)
    deque.pop()
    deque.pop()
    deque.dequeue()
    deque.dequeue()
    stdio.writeln(deque.isEmpty())
    stdio.writeln(deque)

if __name__ == '__main__':
    main()
