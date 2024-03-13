"""

    MINI PROJECT 1
    Class Implementation for Student Information
    Objective:
        Your task is to create a Python class to manage student information. The
        class should have attributes for the student's name, age, gender, and a list
        of marks. Additionally, you need to implement various methods to
        manipulate and display this information.
    Class Structure:
        Your class should be named Student and should contain the following
        attributes:
        name (str): Name of the student.
        age (int): Age of the student.
        gender (str): Gender of the student ('Male', 'Female', or 'Other').
        marks (list of int): List of marks obtained by the student.

    displayAllInfo(): This method should print all information about the
    student, including name, age, gender, and marks.
    displayOnlyMarks(): This method should print only the marks obtained
    by the student.
    getTotal(): This method should return the total marks obtained by the
    student.
    getMax(): This method should return the maximum marks obtained by
    the student.
    getMini(): This method should return the minimum marks obtained by
    the student.
    getAvg(): This method should return the average marks obtained by the
    student.
    addMark(mark): This method should add a new mark to the list of
    marks for the student.
    removeMark(): This method should remove the last mark from the list
    of marks for the student.
    Implement the Student class according to the provided specifications.
    Instantiate the Student class with using a __init__() method. Ask the
    details and 5 marks within __init__().
    Test your class by creating instances of Student and calling various
    methods on them to ensure they work correctly.
    Use meaningful variable names and include comments where
    necessary to enhance code readability.
"""


class Student:
    def __init__(self) -> None:
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: ")
        self.marks = []
        print("Enter marks for 5 subjects: ")
        for _ in range(1, 6):
            marks = int(input(f"Enter {_} subject marks: "))
            self.marks.append(marks)

    def displayAllInfo(self):
        print("Student Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Marks: {self.marks}")

    def displayOnlyMarks(self):
        print("Student Marks:")
        print(f"Marks: {self.marks}")

    def getTotal(self):
        return sum(self.marks)

    def getMax(self):
        return max(self.marks)

    def getMin(self):
        return min(self.marks)

    def getAvg(self):
        return sum(self.marks) / len(self.marks)

    def addMark(self, mark):
        self.marks.append(mark)

    def removeMark(self):
        if self.marks:
            self.marks.pop()
        else:
            print("No marks to remove.")


if __name__ == "__main__":
    student1 = Student()

    student1.displayAllInfo()
    print(f"Total Marks: {student1.getTotal()}")
    print(f"Max Marks: {student1.getMax()}")
    print(f"Min Marks: {student1.getMin()}")
    print(f"Average Marks: {student1.getAvg()}")

    student1.addMark(95)
    print(f"Updated Marks after adding a new mark: {student1.marks}")

    student1.removeMark()
    print(f"Updated Marks after removing the last mark: {student1.marks}")
