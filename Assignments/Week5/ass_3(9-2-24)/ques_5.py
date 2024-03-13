"""
    Q5. Create a Python function to sort a dictionary by its values. And return
that new dictionary.
"""


from typing import Dict


def sortDictionary(dictionary: Dict, reverse=False):
    # print(dictionary.items())   return tuples inside list (1, 2) which we call x to get a value from tuple x[1]--> for values x[0]--> for key
    # sorting based on values  x[1]
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=reverse))


my_dict = {9: 2, 8: 4, 7: 3, 6: 1, 5: 0}
print(f"Ascending order by its values = {sortDictionary(my_dict)}")
