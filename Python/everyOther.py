import stdarray
import stdio
import sys


def main():
    n = int(sys.argv[1])        # get command line integer argument
    a = stdarray.create1D(n, 0)      # initialize array
    b = 0    # variable for final sum of odd numbers

#    if stdio.isEmpty():                     # check standart input

    for i in range(n):             # set loop with step = 2
        x = stdio.readInt()
        a[i] = x

    for i in range(0, n, 2):       # set loop to sum the results
        if i < n - 2:
            b += a[i]
        else:
            b += a[i]
            stdio.writeln(b)       # print out final result
if __name__ == "__main__":
    main()
