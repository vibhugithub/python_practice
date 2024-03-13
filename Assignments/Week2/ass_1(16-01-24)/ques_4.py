"""
    Q4. Attempt Week 1 - Assignment 2 (Q6) and Week 1 - Assignment 2 (Q7)
    using function.
"""


def smallest_number(num1, num2, num3, num4):
    list_num = [num1, num2, num3, num4]
    list_num.sort()

    print(list_num[0])


smallest_number(45, 85, 75, 62)


def salary_increment(salary):
    if salary < 10000:
        increment_percentage = 5
    elif 10000 < salary < 20000:
        increment_percentage = 10
    elif 20000 < salary < 50000:
        increment_percentage = 15
    else:
        increment_percentage = 20

    increment = (salary * increment_percentage) / 100
    increment_salary = salary + increment

    print(f"The orignal salary is {salary:.2f}")
    print(f"The increment salary is {increment_percentage}")
    print(f"The updated salary is {increment_salary:.2f}")


salary_input = float(input("Enter current salary: "))

salary_increment(salary_input)
