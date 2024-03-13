"""
    Q4. Make a function named checkArmstrong which accepts an integer n
    from the user. Return True or False if that number is an armstrong number.

    # Example 1
    checkArmstrong (153)
    # Output
    True
    # Reason
    1^3 + 5^3 +3^3 = 153
    # Example 2
    checkArmstrong (407)
    # Output
    True
    # Reason
    4^3 + 0^3 + 7^3 = 407
"""


def checkArmstrong(num: int):
    arm_num = 0
    n = num
    while n > 0:
        remainder = n % 10
        n = n // 10
        arm_num = arm_num + remainder**3
    print(arm_num)
    if num == arm_num:
        return True
    else:
        return False


x = checkArmstrong(153)
print(x)
