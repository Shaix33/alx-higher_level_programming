#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    numArgs = len(sys.argv) - 1
    args = sys.argv
    if numArgs != 3:
        print("Usage: Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if args[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(args[1])
    b = int(args[3])
    print("{} {} {} = {}".format(a, args[2], b, ops[args[2]](a, b)))
