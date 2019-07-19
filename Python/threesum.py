import stdarray
import stdio
import sys


def writeTriples(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) == 0:
                    stdio.writef('%3d %3d %3d\n', a[i], a[j], a[k])


def closeTo(a, x):
    s = []
    answer = []
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                s += [abs((a[i] + a[j] + a[k])-x)]

    array1 = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if abs((a[i] + a[j] + a[k])-x) == min(s):
                    array1.append(
                        str(a[i]) + ' ' + str(a[j]) + ' ' + str(a[k]))

    b = len(array1) - 1
    for i in range(b, len(array1)):
        temp = array1[i]
        a = temp.split()
        count = 0
        for num in a:
            if count == 2:
                stdio.writef('%3d', int(num))
            else:
                stdio.writef('%3d ', int(num))
            count += 1
        stdio.writeln()

    return


def main():
    x = int(sys.argv[1])
    a = []
    while not stdio.isEmpty():
        a += [stdio.readInt()]
    writeTriples(a)
    stdio.writeln()
    closeTo(a, x)

if __name__ == '__main__':
    main()
