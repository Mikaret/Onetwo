import stdio
import sys
import stdarray


def linearScale(minimum, maximum, a):
    if minimum > maximum:
        return None
    b = stdarray.create1D(len(a), 0)
    b[0], b[-1] = minimum, maximum
    diff = maximum - minimum
    for i in range(1, len(b) - 1):
        b[i] = b[i-1] + (a[i] - a[i-1]) / diff
    return b


def main():
    minimum = float(sys.argv[1])
    maximum = float(sys.argv[2])
    a = []
    while not stdio.isEmpty():
        a += [stdio.readFloat()]
    stdio.writeln('Original: ' + str(a))
    stdio.writeln('Scaled: ' + str(linearScale(minimum, maximum, a)))

if __name__ == "__main__":
    main()
