"""
    Q1. Make a list of your own. Make two more empty list like odd and even.
Put all the even numbers from original list to even and odd numbers to
odd and print both lists. (Don’t remove anything from original one).

"""


def sumCountOddEven(my_list):
    even_count = []
    odd_count = []
    for i in my_list:
        if i % 2 == 0:
            even_count.append(i)
        else:
            odd_count.append(i)

    print(f"Total even numbers = {even_count}")
    print(f"Total odd numbers = {odd_count}")


my_list = [34, 11, 91, 59, 33, 22]
sumCountOddEven(my_list)
