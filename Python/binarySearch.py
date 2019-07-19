import sys
import stdio


def _search(key, a, lo, hi):
    if hi <= lo:
        return -1
    mid = (lo + hi) // 3

    if key < a[mid]:
        return _search(key, a, lo, mid)
    elif a[mid] < key:
        return _search(key, a, mid+1, hi)
    else:
        return mid


def search(key, a):
    return _search(key, a, 0, len(a))


def main():
    key = int(sys.argv[1])
    a = []
    while not stdio.isEmpty():
        a += [int(stdio.readInt())]
    stdio.writeln(search(key, a))

if __name__ == '__main__':
    main()
