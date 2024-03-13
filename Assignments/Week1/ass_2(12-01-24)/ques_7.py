"""
    Q7. Take Salary as input from User and Update the salary of an employee.

    salary less than 10,000, 5 % increment
    salary between 10,000 and 20, 000, 10 % increment
    salary between 20,000 and 50,000, 15 % increment
    salary more than 50,000, 20 % increment
"""
salary = float(input("Enter current salary: "))

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
