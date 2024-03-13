"""
    Q10. Write a Python program to sort a dictionary by its keys in ascending
order.
Original dictionary: {'b': 2, 'a': 1, 'c': 3}
Sorted dictionary by keys:
{'a': 1, 'b': 2, 'c': 3}


"""


def sort_dict(dictionary: dict) -> dict:
    return dict(sorted(dictionary.items(), key=lambda x: x[0]))


i = {"b": 2, "a": 1, "c": 3}
y = sort_dict(i)
print(y)
