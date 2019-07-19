import stdio
import sys


def isPower(n):
    return n != 0 and ((n & (n - 1)) == 0)  # check if n is power of 2


def main():
    n = int(sys.argv[1])		# Get input integer n
    stdio.writeln(isPower(n))   # Print out final result

if __name__ == '__main__':
    main()
