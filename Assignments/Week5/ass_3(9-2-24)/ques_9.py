"""
    Q9. Write a program in Python to calculate the average score of each
student across multiple subjects stored in a dictionary of dictionaries.
Student scores:
{
'John': {'Math': 85,
'Science': 90,
'English': 80},
'Alice': {'Math': 75,
'Science': 88,
'English': 92},
'Bob': {'Math': 90,
'Science': 85,
'English': 78}
}
"""
from typing import Dict


def averageScore(dictionary: Dict) -> None:
    for key, marks in dictionary.items():
        total = marks.get("Math", 0) + marks.get("Science", 0) + marks.get("English", 0)
        average = total / 3
        print(f"{key} = {average}")


averageScore(
    {
        "John": {"Math": 85, "Science": 90, "English": 80},
        "Alice": {"Math": 75, "Science": 88, "English": 92},
        "Bob": {"Math": 90, "Science": 85, "English": 78},
    }
)
