#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":

    sum = 0
    for s in range(len(argv) - 1):
        sum += int(argv[s + 1]) 
    print("{}".format(sum))
