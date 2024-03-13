"""
    Q4. Write a Python program to Convert two lists into a dictionary
Sample Output
keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]
Convert Two List to Dict = {'One' : 1, 'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5}
"""


def merge(keys: list, values: list) -> None:
    new_dict = {}
    for i in range(len(keys)):
        new_dict[keys[i]] = values[i]
    print(new_dict)


keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]

merge(keys, values)
