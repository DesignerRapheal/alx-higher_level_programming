#!/usr/bin/python3

# author - designerrapheal

def complex_delete(a_dictionary, value):
    listed_keys = list(a_dictionary.keys())

    for value_dic in listed_keys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return (a_dictionary)
