#!/usr/bin/python3
import sys
if __name__ == "__main__":

    numArgs = len(sys.argv) - 1
    if numArgs == 0:
        print(numArgs, "arguments.")
    elif numArgs == 1:
        print(numArgs, "argument:".format(sys.argv[0]))
        print("1:", sys.argv[1])
    else:
        print(numArgs, "arguments:")
        for x in range(1, numArgs + 1):
            print("{}: {}".format(x, sys.argv[x]))
