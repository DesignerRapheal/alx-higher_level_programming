#!/usr/bin/python3

# author - designerrapheal

def best_scores(a_dictionary):
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key=a_dictionary.get))
