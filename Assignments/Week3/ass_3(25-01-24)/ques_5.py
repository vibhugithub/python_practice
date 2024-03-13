"""
    Q5. Create a function updateOddEven that accepts an List of Integers and
    update all the even numbers to 0 and update all the odd numbers to 1.

    my_list = [34, 11, 91, 59, 33, 22]
    updateOddEven (my_list)
    print (my_list)
    # Output
    [0, 1, 1, 1, 1, 0]
"""


def updateOddEven(my_list):
    count = []
    for i in my_list:
        if i % 2 == 0:
            count.append(0)
        else:
            count.append(1)
    return count


ll = [34, 11, 91, 59, 33, 22]
x = updateOddEven(ll)
print(x)
