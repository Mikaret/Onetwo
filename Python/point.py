import stdio
import sys
import math


class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def distanceTo(self, other):
        x0 = (other._x - self._x)**2
        y0 = (other._y - self._y)**2
        y = math.sqrt(x0+y0)
        return y

    def __str__(self):
        return '(' + str(self._x) + ', ' + str(self._y) + ')'


def _main():
    x1, y1, x2, y2 = map(float, sys.argv[1:])
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    stdio.writeln('p1 = ' + str(p1))
    stdio.writeln('p2 = ' + str(p2))
    stdio.writeln('d(p1, p2) = ' + str(p1.distanceTo(p2)))

if __name__ == '__main__':
    _main()
