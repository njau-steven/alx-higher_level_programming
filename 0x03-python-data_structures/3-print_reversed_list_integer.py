#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    reverse = my_list[:: -1]

    for i in range(len(reverse)):
        print("{:d}".format(reverse[i]))
