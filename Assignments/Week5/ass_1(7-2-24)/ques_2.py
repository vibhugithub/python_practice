"""
    Q2. Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject with highest marks
scored.

"""

marks = {
    "physics": 67,
    "comp": 10,
    "science": 99,
    "english": 82,
    "hindi": 17,
}
print(list(max(marks.items())))
