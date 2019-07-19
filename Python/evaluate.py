import stdio
import sys
import math
from linkedstack import Stack
from linkedstack import _Node

ops = Stack()     # Initialize Stack for operations
values = Stack()   # Initialize Stack for values

while not stdio.isEmpty():
    arg = stdio.readString()  # Assign input string to arg
    if arg == '+':            # Consider all operators
        ops.push(arg)
    elif arg == '-':
        ops.push(arg)
    elif arg == '*':
        ops.push(arg)
    elif arg == 'sqrt':
        ops.push(arg)
    elif arg == ')':         # When brackets closes...
        op = ops.pop()       # Perform operation...
        value = values.pop()
        if op == '+':
            value = values.pop() + value
        if op == '-':
            value = values.pop() - value
        if op == '*':
            value = values.pop() * value
        if op == 'sqrt':
            value = math.sqrt(value)
        values.push(value)   # Add result to the value stack
    elif arg != '(':
        values.push(float(arg))
stdio.writeln(values.pop())
