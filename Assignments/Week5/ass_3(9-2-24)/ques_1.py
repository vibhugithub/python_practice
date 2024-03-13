"""
    Q1. Write a Python script to sort (ascending and descending) a dictionary
by value.
Sample Output
dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
Ascending order = { 0:0, 2:1, 1: 2, 3: 4}
Descending order = {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
"""

from typing import Dict


def sortDictionary(dictionary: Dict, reverse=False):
    # print(dictionary.items())   return tuples inside list (1, 2) which we call x to get a value from tuple x[1]--> for values x[0]--> for key
    # sorting based on values  x[1]
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=reverse))


my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(f"Ascending order = {sortDictionary(my_dict)}")
print(f"Descending order = {sortDictionary(my_dict,reverse=True)}")
