"""
    Q1. Given a list of strings, concatenate them into a single string separated
by spaces. For example, given the input ["Hello", "World", "Python"], the
output should be "Hello World Python".
Make a list on your own.
Don’t use the JOIN function.
"""


def concatenate(l: list) -> None:
    new = ""
    for i in l:
        new += i
        new += " "

    print(new)


l = ["Hello", "World", "Python"]
concatenate(l)
