#!/usr/bin/python3
for x in range(122, 96, -1):
    if x % 2 == 1:
        y = chr(x - 32)
        print(y, end="")
    else:
        print("{}".format(chr(x)), end="")
