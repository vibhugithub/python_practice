"""
    Q5. Write a Python program to combine two dictionary by adding values
for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
"""


def merge_dict(dict1, dict2):
    new_dict = {}
    # for k, v in dict1.items():
    #     list_v = v + dict2.get(k, 0)
    # new_dict[k] = list_v

    for key in dict1.keys() | dict2.keys():
        new_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)
    return new_dict


dict_1 = {"A": 100, "B": 200}
dict_2 = {"A": 100, "B": 200}

merged_dict = merge_dict(dict_1, dict_2)
print(merged_dict)
