import stdio
import sys


class LinkedList:

    def __init__(self):
        self._first = None
        self._last = None

    def isEmpty(self):
        return self._first is None

    def add(self, item):
        oldLast = self._last
        self._last = _Node(item, None)
        if self.isEmpty():
            self._first = self._last
        else:
            oldLast.next = self._last

    def find(self, item):
        cur = self._first
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def __str__(self):
        s = ''
        cur = self._first
        while cur is not None:
            s += str(cur.item) + ' '
            cur = cur.next
        return s


class _Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


def main():
    key = int(sys.argv[1])
    list = LinkedList()
    while not stdio.isEmpty():
        item = stdio.readInt()
        list.add(item)
    stdio.writeln(list.find(key))

if __name__ == '__main__':
    main()
