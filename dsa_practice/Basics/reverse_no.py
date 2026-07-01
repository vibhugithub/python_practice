import math

"""
not nice approch
    a=str(1234)
    a[::-1]
    a=int(a)
"""
"""
Time complexity=O(n)
space=O(1)
"""


def reverse_number_(n: int):
    reverse = ""
    while n > 0:
        remainder = n % 10
        reverse += str(remainder)
        n = n // 10
    print(reverse)


reverse_number_(123456)
"""
Time complexity=O(log10(n))
space=O(1)
"""


def reverse_number(n):
    # Handle negative numbers
    sign = -1 if n < 0 else 1
    n = abs(n)

    reversed_n = 0
    while n > 0:
        # Extract the last digit
        digit = n % 10
        # Build the reversed number
        reversed_n = reversed_n * 10 + digit
        # Remove the last digit
        n //= 10

    # Restore the sign
    reversed_n *= sign

    return reversed_n


# Example usage
number = 12345
reversed_number = reverse_number(number)
print("Original number:", number)
print("Reversed number:", reversed_number)


class Solution:
    def reverse(self, x: int) -> int:
        min_x=-2**31
        max_x=2**31-1
        sign=-1 if x<0 else 1
        x=abs(x)

        reverse=0
        while x>0:
            print("max",max_x,"min",min_x)
            if reverse>max_x or reverse <min_x:
                print("returnnnn",reverse)
                return 0
            remainder = x%10
            reverse=reverse*10+remainder
            x=x//10
            print("reverse",reverse)
        print("sign*reverse",sign*reverse)
        return sign*reverse

# Create an instance of Solution
sol = Solution()

# Call the reverse method on the instance
result = sol.reverse(1534236469)
print(result)