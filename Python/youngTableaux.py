import stdarray
import stdio
import sys


def isYoung(a):
    young = False
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i != len(a) - 1:
                if not a[i][j] < a[i + 1][j]:
                    return False
            elif j != len(a[0]) - 1:
                if not a[i][j] < a[i][j + 1]:
                    return False
            else:
                young = True
    return young


def isContains(a, x):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == x:
                return True
    return False


def main():
    row = int(sys.argv[1])
    col = int(sys.argv[2])
    a = stdarray.create2D(row, col)
    for i in range(row):
        for j in range(col):
            a[i][j] = stdio.readInt()
    if not isYoung(a):
        stdio.writeln(False)
    if isYoung(a):
        x = 73
        stdio.writeln(isContains(a, x))

if __name__ == '__main__':
    main()
