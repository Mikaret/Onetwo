import stdio
import sys


def isValid(isbn):
    nmbs = isbn.replace("-", "")
    nbts = nmbs[:-1]
    n = map(str, nbts)
    n = ''.join(n)
    n = int(n)

    if len(nmbs) != 10:
        return False
    total = 0
    for i in range(2, 11):
        digit = n % 10   # rightmost digit
        total += i * digit
        n //= 10

    z = nbts
    if total % 11 == 1:
        z += 'X'
    elif total % 11 == 0:
        z += '0'
    else:
        z += str(11 - (total % 11))

    if nmbs == z:
        return True
    else:
        return False


def _main():
    isbn = sys.argv[1]
    stdio.writeln(isValid(isbn))

if __name__ == '__main__':
    _main()
