"""
    Q2. A student will not be allowed to sit in exam if his/her attendance is less
    than 75%.
    Take following input from user
    Number of classes held
    Number of classes attended.
    1. Print percentage of class attended
    2. Print Is student is allowed to sit in exam or not
"""
total_classes = int(input("Enter total number of class: "))
attend_classes = int(input("Enter number of classes you were attend: "))

percentage = int((attend_classes / total_classes) * 100)

print(f"{percentage} % of class attended")

if percentage >= 75:
    print("You'r allowed to sit in exam")
else:
    print("Not allowed to sit in exam")
