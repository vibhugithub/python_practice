"""
Q3. Employee Class with Performance Evaluation
Attributes:
name: Name of the employee.
age: Age of the employee.
gender: Gender of the employee.
phone: Phone number of the employee.
salary: Salary of that employee
Methods:
__init__(self, name, age, gender, phone,salary): Constructor method to
initialize the employee object with name, age, gender, and phone number,
salary attributes.
change_salary(self): Method that asks within the new salary and updates
the salary of that employee
display_details(self): Method to display all details of the employee,
including name, age, gender, phone number, salary.
"""


class Employee:
    def __init__(self, name, age, gender, phone, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.salary = salary

    def change_salary(self):
        new_salary = float(input("Enter the new salary: "))
        self.salary = new_salary

    def display_details(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Phone:", self.phone)
        print("Salary:", self.salary)


# Example usage:
employee1 = Employee("John", 30, "Male", "1234567890", 50000)
employee1.display_details()
print()

employee1.change_salary()
print("After salary change:")
employee1.display_details()
