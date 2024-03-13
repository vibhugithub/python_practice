"""
    Q1. Create a function named div_by_3_and_5 which takes 2 integers as a
arguments (n1,n2), and print all the numbers divisible by 3 and 5 between
n1 and n2.

"""


def div_by_3_and_5(n1, n2):
    if n1 > n2:
        n1, n2 = n2, n1

    divisible_numbers = [i for i in range(n1, n2 + 1) if i % 3 == 0 and i % 5 == 0]

    print(divisible_numbers)


div_by_3_and_5(1, 60)


########### ANOTHER APPROACH
def div_by_3_and_5_(n1: int, n2: int):
    i: int = n1
    while i <= n2:
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")
        i += 1
    print()
