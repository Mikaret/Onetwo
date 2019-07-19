import stdio
import sys


def ackermann(m, n):
    if m == 0:
        return n+1
    if m > 0 and n == 0:
        return ackermann(m-1, 1)
    if m > 0 and n > 0:
        return ackermann(m-1, ackermann(m, n-1))


def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    stdio.writeln(ackermann(m, n))

if __name__ == "__main__":
    main()
