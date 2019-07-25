import stdio
import sys


def power(a, b):                    # define function for a and b values
    if b == 0:                      # define condition for power = 0
        return 1
    if b % 2 == 0:                  # condition if b is odd
        return a * power(a, b-1)
    if b % 2 > 0:
        return (a**2) * power(a, b/2)  # condition if b is even


def _main():                        # define test part
    a = int(sys.argv[1])            # get a value as argument
    b = int(sys.argv[2])            # get b value as argument
    stdio.writeln(power(a, b))      # print out the result

if __name__ == '__main__':          # end of test part
    _main()
