#!/usr/bin/python3
import sys
if __name__ == "__main__":
    numArgs = len(sys.argv)
    result = 0
    args = sys.argv
    for i in range(1, numArgs):
        result = result + int(args[i])
    print(result)
