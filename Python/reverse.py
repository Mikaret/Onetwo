import stdio
from linkedstack import Stack
from linkedstack import _Node

stack = Stack()   # Create Stack for Input arguments
count = 0
while not stdio.isEmpty():   # Push arguments of input to Stack
    stack.push(stdio.readString())
    count += 1

for i in range(count):   # Pop results from Stack and pop them
    word = stack.pop()
    stdio.writeln(word)
