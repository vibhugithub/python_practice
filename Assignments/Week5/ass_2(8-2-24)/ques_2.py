"""
    Create a function named countChar which will accept a string as a
parameter. Create a dictionary having frequency of each character.

"""


def count_char(string: str):
    new_dict = {}
    for i in string:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    print(new_dict)


count_char("hheelllooo")
