"""
    Q3. Write a Python function that takes a dictionary as input where the
    values are lists of integers. The function should return a new dictionary
    where the values are lists containing only the even integers from the
    original lists.

"""


input_dict = {"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]}


def new_list(my_dict: dict) -> None:
    res = []
    for k, v in my_dict.items():
        for i in v:
            if i % 2 != 0:
                v.remove(i)
    # filtered_dict = {}
    # for key, value in my_dict.items():  # Optimal Way
    #     filtered_dict[key] = [num for num in value if num % 2 == 0]
    # print( filtered_dict)

    print(my_dict)


new_list(input_dict)
