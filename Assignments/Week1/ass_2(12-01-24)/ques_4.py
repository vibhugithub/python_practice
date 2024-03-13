"""
    Q4. Write a Python program that takes a student's score as input and
    prints the corresponding grade. Use the following grading scale:
    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    F: Below 60
"""
num = int(input("Enter number to check grade: "))

# num >= 90 and num <= 100

if 90 <= num <= 100:
    print("YAYYY!! grade A")
elif 80 <= num <= 89:
    print("Wow!! grade B")
elif 70 <= num <= 79:
    print("Keep it up!! grade C")
elif 60 <= num <= 69:
    print("grade D")
elif num < 60:
    print("grade F")
