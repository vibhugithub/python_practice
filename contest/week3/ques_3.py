"""
    Q3. Write a function named armstrongRange which accepts 2 integers n1
and n2. Print all the numbers from n1 to n2 which are armstrong numbers.
Example
Enter the starting number: 56
Enter the ending number: 1000
Armstrong numbers between 56 and 1000 are:
153
370
371
407
"""


def armstrongRange(n1, n2):
    def is_armstrong(num):
        # Convert the number to a string to count its digits
        num_str = str(num)
        num_digits = len(num_str)

        # Calculate the sum of each digit raised to the power of the number of digits
        total = sum(int(digit) ** num_digits for digit in num_str)

        # Check if the total is equal to the original number
        return total == num

    # Print Armstrong numbers within the range
    print(f"Armstrong numbers between {n1} and {n2} are:")
    for num in range(n1, n2 + 1):
        if is_armstrong(num):
            print(num)


# Example usage:
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))
armstrongRange(start_num, end_num)
