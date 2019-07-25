import stdio
import sys


def zeros(s):                    # define function to count zeros
    if len(s) == 0:              # base case, empty string
        return 0
    if s[0] == '0':              # condition to count zeros
        return zeros(s[1:]) + 1  # if zero, count 1, slice 1
    else:
        return zeros(s[1:]) + 0  # if not zero, just slice 1


def ones(s):                     # define function to count ones
    if len(s) == 0:              # base case, empty string
        return 0
    if s[0] == '1':              # condition to count ones
        return ones(s[1:]) + 1   # if one, count 1, slice 1
    else:
        return ones(s[1:]) + 0   # if not one, just slice 1


def _main():                     # define test part
    s = str(sys.argv[1])         # get string argument s
    stdio.write('zeros = ' + str(zeros(s)) + ',')  # print zeros
    stdio.write(' ones = ' + str(ones(s)) + ',')   # print ones
    stdio.writeln(' total = ' + str(len(s)))       # print total

if __name__ == '__main__':       # end of test part
    _main()
