import stdio
import sys
import stdarray


def gcd(x, y):
    while y:
        r = x % y
        x = y
        y = r
    return x


def main():
    n = int(sys.argv[1])
    mat = stdarray.create2D(n, n, False)
    for i in range(n):
        for j in range(n):
            if gcd(i + 1, j + 1) == 1:
                mat[i][j] = True
    for i in range(n):
        for j in range(n):
            if mat[i][j]:
                stdio.write('*')
            else:
                stdio.write(' ')
        stdio.writeln()

if __name__ == "__main__":
    main()
