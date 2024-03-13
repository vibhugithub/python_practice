"""
    Q11. Write a python program which prints all the values whose count is
greater than 3. (Make sure to make a list with at least 15 numbers)
"""


def listgreaterthree(l):
    result = []
    if len(l) > 3:
        for i in l:
            result.append(i)
    print(result)


user_list = [5, 1, 5, 5, 25, 65, 25, 85]
listgreaterthree(user_list)
