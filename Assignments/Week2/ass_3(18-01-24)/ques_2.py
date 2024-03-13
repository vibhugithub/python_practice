"""
    2. Create a function named calSum() which takes 2 integers n1 and n2 as
a argument. Calculate the sum of all the numbers from n1 and n2 and
RETURN THAT SUM. Also make sure that n1 is smaller than n2. If it is not,
then return “n1 should be smaller”.

"""


def calSum(n1, n2):
    sum = 0
    if n1 > n2:
        n1, n2 = n2, n1
    i = n1
    while i <= n2:
        sum += i
        i += 1
    print(sum)


calSum(7, 3)
