"""
    Q3. Create a function named pattern which takes an integer as an input
    and print the following pattern.
    
    # Example 1
    pattern (4)
    # Output
    1 2 4 8

    # Example 2
    pattern (7)
    # Output
    1 2 4 8 16 32 64 # Basically print upto 7 numbers
"""


def pattern(n: int):
    i = 1
    num = 1
    while n >= i:
        print(num, end=" ")
        num = num + num
        i += 1


pattern(7)
