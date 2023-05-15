#!/usr/bin/python3

# Function to replace an element of a list at a specific position like c.# author - designerrapheal

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
