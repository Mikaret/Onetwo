import stdio
import sys


def main():
    n = int(sys.argv[1])
    if n <= 0:
        stdio.write(None)

    for i in range(1, n+1):
        if i > 1:
            stdio.writeln()
        for j in range(1, n*2):
            if (i+j) % 2 != 0:
                stdio.write(' ')
            if (i+j) % 2 == 0:
                stdio.write('*')
    stdio.writeln()

if __name__ == "__main__":
    main()
