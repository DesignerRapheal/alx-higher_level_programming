#!/usr/bin/python3

# author - designerrapheal

def simple_delete(my_dict, key=""):
    if key in my_dict:
        del my_dict[key]
    return my_dict
