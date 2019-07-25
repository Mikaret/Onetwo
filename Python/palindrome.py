import stdio
import sys


def is_palindrome(s):                # define function
    if len(s) < 2:                   # set condition for single letter
        return True
    if s[0] != s[-1]:                # check last & first letters
        return False
    return is_palindrome(s[1:-1])    # slice out right/leftmost letters


def _main():                         # define test part
    s = str(sys.argv[1])             # get string argument s
    stdio.writeln(is_palindrome(s))  # print out result of the function

if __name__ == '__main__':           # end of test part
    _main()
