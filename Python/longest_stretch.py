import stdio
import sys


def main():

    a = []								# initialize array
    count = 1 							# counter renewable
    best = 0 							# value of longest sequence
    TopCount = 0						# final counter for longest sequence

    for i in range(1, len(sys.argv)):   # get numbers from command line
        a += [int(sys.argv[i])]         # fill in array elements

    for i in range(len(a) - 1):			# Set loop to iterate through array

        if a[i] == a[i+1]:              # Distinguish equal values
            count += 1                  # Count equal values

            if count > TopCount:		# Compare the length of equal values
                TopCount = count		# Longest stretch set to TopCounter
                best = a[i]				# Distinguish the champion value
        else:
            count = 1					# Othervise - renew counter

    if TopCount > 1:					# Print out if there were equal values

        stdio.writeln(str(TopCount) + ' consecutive ' + str(best) + 's')

    else:								# Print out if there were no equal values
        stdio.writeln(str(1) + ' consecutive ' + str(a[0]) + 's')

if __name__ == "__main__":
    main()
