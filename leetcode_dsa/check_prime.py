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

#optimal way
'''
TC -> 0(sqrt (n)b
SC -> 0(1)
'''
from math import sqrt
def checkPrime(num: int) -> int:
    print("sqrt(num)",int(sqrt(num)))
    for i in range(2, int(sqrt(num)) + 1):
        print(num%i,num,i)
        if num % i == 0:
            return False
    return True
print(checkPrime(4))
#brute force
'''
TC-> 0(n)
SC-> 0(1)
'''

def checkPrime(num: int)-> int:
    for i in range (2, num) :
        if num % i == 0:
            return False
    return True
# print(checkPrime (2))
# print(checkPrime(3))