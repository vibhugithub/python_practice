"""
Q7. Make two lists of same length and pass it to a function. Return a third
list where each element is the sum of index.

lst1 = 110, 25, 30, -10, 1, 91
lst2 = 158, 11, -15, 20, 6, 11
result = addition(lst1,lst2)
print (result)
# Output
[68, 36, 15, 10, 7, 10]
"""


def addition(lst1, lst2):
    new_l = []
    l = len(lst1)
    print(l)
    for i in range(0, l):
        # print(i, lst1[i], lst2[i])
        s = lst1[i] + lst2[i]
        new_l.append(s)

    print(new_l)


lst1 = [10, 25, 30, -10, 1, 9]
lst2 = [58, 11, -15, 20, 6, 1]
result = addition(lst1, lst2)
