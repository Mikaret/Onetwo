import stdio
import sys


class Interval:

    def __init__(self, lbound, ubound):
        self._lbound = float(lbound)
        self._ubound = float(ubound)

    def lbound(self):
        return self._lbound

    def ubound(self):
        return self._ubound

    def contains(self, x):
        if x <= self._ubound and x >= self._lbound:
            return True
        else:
            return False

    def intersects(self, other):
        if (other._lbound <= self._ubound):
            return True
        else:
            return False

    def __str__(self):
        return "[" + str(self._lbound) + ", " + str(self._ubound) + "]"

i = Interval(2, 8)


def _main():
    x = float(sys.argv[1])
    intervals = []
    while not stdio.isEmpty():
        lbound = stdio.readFloat()
        ubound = stdio.readFloat()
        intervals += [Interval(lbound, ubound)]
    for i in range(len(intervals)):
        if intervals[i].contains(x):
            stdio.writef('%s contains %f\n', intervals[i], x)
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i].intersects(intervals[j]):
                stdio.writef('%s intersects %s\n', intervals[i], intervals[j])

if __name__ == '__main__':
    _main()
