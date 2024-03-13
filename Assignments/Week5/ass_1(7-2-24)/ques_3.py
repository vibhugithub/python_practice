"""
    Q3. Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject which has marks
more than passing marks (above 33)
"""

marks = {
    "physics": 67,
    "comp": 10,
    "science": 99,
    "english": 82,
    "hindi": 17,
}

for k, v in marks.items():
    if v > 33:
        print(f"{k} and marks is {v}")
