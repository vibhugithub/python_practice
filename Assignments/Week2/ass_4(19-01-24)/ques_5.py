"""
    Q5. Keep asking numbers from user until the user enters 0. Then display
the average of all numbers.
"""


def average():
    num = 0
    count = 0
    while True:
        n = int(input("Enter a number (enter 0 to finish):"))
        if n == 0:
            break
        num = num + n
        count += 1

    print(num / count)


average()
