import stdio
import sys


def _gcd(p, q):
    return p if q == 0 else _gcd(q, p % q)


class Rational:

    def __init__(self, x, y=1):
        g = _gcd(x, y)
        self.n = x / g
        self.d = y / g

    def __add__(self, other):
        return Rational(self.n * other.d + other.n * self.d,
                        self.d * other.d)

    def __sub__(self, other):
        return Rational(self.n * other.d - other.n * self.d,
                        self.d * other.d)

    def __mul__(self, other):
        return Rational(self.n * other.n, self.d * other.d)

    def __abs__(self):
        return Rational(self.n * other.d, self.d * other.n)

    def __str__(self):
        a, b = self._x, self._y
        if a == 0 or b == 1:
            return str(a)
        if b < 0:
            a *= -1
            b *= -1
        return str(a) + '/' + str(b)


def _main():
    n = int(sys.argv[1])
    total = Rational(0)
    sign = Rational(1)
    for i in range(1, n + 1):
        total += sign * Rational(1, 2 * i - 1)
        sign *= Rational(-1)
    stdio.writeln(4.0 * total.n / total.d)

if __name__ == '__main__':
    _main()
