"""
Q1. Create a class called Employee with attributes such as name, age,
gender, and phone number. Implement a constructor to initialize these
attributes.
Include methods to calculate monthly and yearly salary based on hourly
rate and hours worked. Ask hourly rate and hours worked inside the
method (local variable).
Create 2 objects and check your code.
"""


class Employee:
    def __init__(self, name, age, gender, phone_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number

    def calculate_monthly_salary(self, hourly_rate, hours_worked):
        monthly_salary = hourly_rate * hours_worked
        return monthly_salary

    def calculate_yearly_salary(self, hourly_rate, hours_worked):
        yearly_salary = self.calculate_monthly_salary(hourly_rate, hours_worked) * 12
        return yearly_salary


# Example usage:
emp1 = Employee("John Doe", 30, "Male", "123-456-7890")
hourly_rate1 = float(input("Enter hourly rate for employee 1: "))
hours_worked1 = float(input("Enter hours worked for employee 1: "))
monthly_salary1 = emp1.calculate_monthly_salary(hourly_rate1, hours_worked1)
print("Monthly salary for employee 1:", monthly_salary1)
yearly_salary1 = emp1.calculate_yearly_salary(hourly_rate1, hours_worked1)
print("Yearly salary for employee 1:", yearly_salary1)

emp2 = Employee("Jane Smith", 25, "Female", "987-654-3210")
hourly_rate2 = float(input("Enter hourly rate for employee 2: "))
hours_worked2 = float(input("Enter hours worked for employee 2: "))
monthly_salary2 = emp2.calculate_monthly_salary(hourly_rate2, hours_worked2)
print("Monthly salary for employee 2:", monthly_salary2)
yearly_salary2 = emp2.calculate_yearly_salary(hourly_rate2, hours_worked2)
print("Yearly salary for employee 2:", yearly_salary2)
