import stdio
import sys


def lcm(x, y):

    if x == 0:      # check if neither of numbers are zero
        return 0
    if y == 0:
        return 0

    if x < 0:        # check if neither of numbers are below 0
        return None
    if y < 0:
        return None

    if x > y:       # Compare x and y and chose the greater number...
        gr8r = x    # ... and assin it to variable gr8r
    else:
        gr8r = y

    while(True):   # initiate an infinite loop
        if((gr8r % x == 0) and (gr8r % y == 0)):  # check both numbers
            lcm = gr8r   # if both numberes divide current number...
            break        # assign them to lcm variable and break
        gr8r += 1        # counter for loop, increasing its number by 1

    return lcm


def main():
    x = int(sys.argv[1])             # get input int argument x
    y = int(sys.argv[2])             # get input int argument y

    stdio.writeln(lcm(x, y))

if __name__ == '__main__':
    main()
