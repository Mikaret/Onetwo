import stdio
import sys
from linkedqueue import Queue
from linkedqueue import _Node

n = int(sys.argv[1])  # Command line argument assigned to n
letters = Queue()     # Preset Queue for input
count = 0             # Counter to find exact argument
while not stdio.isEmpty():   # Loop till all arguments read
    letters.enqueue(stdio.readString())  # Add letters to Queue
    count += 1        # Counter tick

a = count - n         # Set variable to get the needed argument
for i in range(a):    # Loop for dequeq
    letters.dequeue()  # Dequeue

stdio.writeln(letters.dequeue())  # Print result
