#!/usr/bin/python3

# author - designerrapheal

def weight_average(the_list=[]):
    if not the_list:
        return 0

    num = 0
    den = 0

    for tup in the_list:
        num += tup[0] * tup[1]
        den += tup[1]

    return (num / den)
