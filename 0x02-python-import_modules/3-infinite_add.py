#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_compte = len(sys.argv) - 1
    res = 0
    for x in range(arg_compte):
        res += int(sys.argv[x + 1])
    print(res)
