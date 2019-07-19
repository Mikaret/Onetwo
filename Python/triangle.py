import stdio
import sys
import stdarray


def areTriangular(a, b, c):
    if a >= b + c:
        return False
    if b >= a + c:
        return False
    if c >= a + b:
        return False
    else:
        return True


def main():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    stdio.writeln(areTriangular(a, b, c))

if __name__ == "__main__":
    main()
