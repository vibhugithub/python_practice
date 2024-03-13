"""
    Q2. Write a Python program to count number of items in a dictionary value
that is a list.
Sample Output
Dict = { 'M1' : [67, 79, 90, 73, 36], 'M2' : [89, 67, 84], 'M3' : [82, 57] }
Number of Items in a Dictionary : 10

"""


def count(dictionary: dict):
    count = 0
    for key, value in dictionary.items():
        count = count + len(value)
    print(count)
    # values = dictionary.values()
    # new_list = []
    # for i in values:
    #     new_list.extend(i)
    # print(len(new_list))


Dict = {"M1": [67, 79, 90, 73, 36], "M2": [89, 67, 84], "M3": [82, 57]}
count(Dict)
