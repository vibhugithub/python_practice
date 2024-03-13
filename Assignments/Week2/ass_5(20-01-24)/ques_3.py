"""
    Q3. Ask x and n from user and then calculate the following answer.
    # Example 1
    pattern (x=6,n=4)
    # Output
    6/1 + 6/3 + 6/5 + 6/7
    10.057142857142857 (OUTPUT)
    # Example 2
    pattern (x=9,n=11)
    # Output
    9/1 + 9/3 + 9/5 + 9/7 + 9/9
    19.627871200007426 (OUTPUT)
    ...
    upto n times
"""


def calculate(x: int, n: int):
    total = 1
    i = 1
    sum = 0
    for i in range(n + 1):
        print(f"{x}/{total }", end=" + ")  # just to print pattern 9/1 + 9/3
        sum = sum + x / total
        total += 2
    print()
    print(f"Total sum {sum}")


calculate(9, 11)
