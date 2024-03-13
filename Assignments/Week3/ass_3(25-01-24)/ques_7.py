"""
    Q7. Create a function calculatePrime that accepts an List of Integers and
    print all the prime numbers in that list.
    my_list = [34, 11, 91, 59, 33, 22]
    calculatePrime (my_list)
    # Output
    11 91 59
"""


def is_prime(num: int) -> bool:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


def calculatePrime(lst):
    for i in range(0, len(lst)):
        if is_prime(lst[i]) == True:
            print(lst[i], end=" ")


my_list = [34, 11, 91, 59, 33, 22]
calculatePrime(my_list)
