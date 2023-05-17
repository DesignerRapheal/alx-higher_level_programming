#!/usr/bin/python3

# author - designerrapheal

def print_sorted_dictionary(a_dictionary):
    list_oud = list(a_dictionary.keys())
    list_oud.sort()
    for i in list_oud:
        print("{}: {}".format(i, a_dictionary.get(i)))
