"""
    Q4. Write a Python function that takes two dictionaries as input, where the
    values are lists. The function should merge the lists corresponding to the
    same keys in both dictionaries into a single list and return a new dictionary
    with these merged lists.
"""


def merge_dict(dict1, dict2):
    new_dict = {}
    for k, v in dict1.items():
        list_v = v[:]  # Create a copy of the list to avoid modifying the original list
        if k in dict2:
            list_v.extend(
                dict2.get(k, [])
            )  # Extend the list with values from dict2 if key exists
            new_dict[k] = list_v
        else:
            new_dict[k] = list_v
    return new_dict


dict_1 = {"A": [1, 2, 3], "B": [4, 5, 6], "C": [11, 12]}
dict_2 = {"A": [7, 8], "B": [9, 10]}

merged_dict = merge_dict(dict_1, dict_2)
print(merged_dict)
