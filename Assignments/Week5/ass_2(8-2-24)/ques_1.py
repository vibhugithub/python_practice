"""
    Q1. Write a Python function that takes a dictionary as input where the
    values are lists. The function should return a new list containing all the
    elements from all the lists in the dictionary.
    It should have at least 3-4 keys and any amount of elements can be in a
    list
"""

input_dict = {"A": [1, 2, 3], "B": [4, 5, 6]}


def new_list(my_dict: dict) -> None:
    res = []
    for i in my_dict.values():
        # res.extend(i)             update existing list add data in list
        for v in i:
            res.append(v)
    print(res)


new_list(input_dict)
