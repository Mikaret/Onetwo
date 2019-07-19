import stdio
import sys
import stdarray
from linkedstack import Stack
from linkedstack import _Node

stk = Stack()      # Stack to collect brackets
prt = sys.argv[1]  # Input argument assigned to prt variable

both = True        # Boolean value to check set of brackets

for i in range(len(prt)):      # Loop to iterate through prt
    if prt[i] == "(" or prt[i] == "[" or prt[i] == "{":
        stk.push(prt[i])                  # Add opening brackets
    if prt[i] == ")" or prt[i] == "]" or prt[i] == "}":
        item = stk.pop()                  # Check closing brackets and if...
        if item == "(" and prt[i] != ")":
            both = False                   # ... not present in stack...
        elif item == "[" and prt[i] != "]":
            both = False                    # ... set boolean value to False
        elif item == "{" and prt[i] != "}":
            both = False
        else:
            continue

stdio.writeln(both)
