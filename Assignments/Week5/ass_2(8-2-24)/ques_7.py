"""
    Q7. Store name as a Key, and 5 marks in a List as a value in dictionary. Store
details of at least 5 students. Print the total marks with percentage of each
and every student
    """


def calculatePercentage(marks: int):
    return (marks / 500) * 100


no_students = int(input("How many student data you'll enter: "))
data = []

for i in range(no_students):
    new_dict = {}
    subject_marks = []
    name = input(f"Enter the  name of student:")
    for j in range(1, 5 + 1):
        marks = int(input(f"Enter the {j} subject marks:"))
        subject_marks.append(marks)
    new_dict["name"] = name
    new_dict["marks"] = subject_marks
    data.append(new_dict)

print(data)

for student in data:
    total_marks = sum(student["marks"])
    percentage = calculatePercentage(total_marks)
    print(
        f"Name: {student['name']}, Total Marks: {total_marks}, Percentage: {percentage:.2f}%"
    )
