#!/usr/bin/python3
for n in range(0, 10):
    for j in range(0, 10):
        if n >= j:
            continue
        elif n == 8 and j == 9:
            print("{}{}".format(n, j))
        else:
            print("{}{}, ".format(n, j), end=u"")
