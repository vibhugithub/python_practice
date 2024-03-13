"""
    Q2. Write a function named notPrimeNumbers which accepts 2 integers n1
and n2. Print all the numbers from n1 to n2 which are not prime.
Example
notPrimeNumbers(5,20)
6 8 9 10 12 14 15 16 18 20
"""


def notPrimeNumbers(n1, n2):
    def is_prime(num):
        if num <= 1:
            return False
        print(num, " ", int(num**0.5))
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    not_prime_list = []
    for num in range(n1, n2 + 1):
        if not is_prime(num):
            not_prime_list.append(num)

    print(*not_prime_list, sep=" ")


# Example usage:
notPrimeNumbers(5, 20)
