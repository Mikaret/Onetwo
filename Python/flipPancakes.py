import stdio
import sys


def flipper(a, n):
    if n == 0:
        return n

    else:
        largest = max(a)
        for i in range(a):
            if a[i] == largest
                 l_index = i


#        for i in range(n):
#            if a[i] > largest:
#                largest = a[i]
#                l_index = i
                
        

#        a_t = a[:(l_index + 1)]
#        a_t = a.reverse()
#        a_t += a[(l_index + 1):]
#       a = a_t
        
        return a


def main():
    a = []
    for i in range(1, len(sys.argv)):
        a += [int(sys.argv[i])]
    flipper(a, len(a))
    stdio.writeln(a)

if __name__ == "__main__":
    main()
