"""
Q7. Convert a list of Tuples into Dictionary
Input: [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25),
("ashish", 30)]
Output: {'akash': [10], 'gaurav': [12], 'anand': [14], 'ashish': [30], 'akhil': [25],
'suraj': [20]}
Input: [('A', 1), ('B', 2), ('C', 3)]
Output: {'B': [2], 'A': [1], 'C': [3]}
"""


def convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
        print(di)
    return di


# Driver Code
tups = [
    ("akash", 10),
    ("gaurav", 12),
    ("anand", 14),
    ("suraj", 20),
    ("akhil", 25),
    ("ashish", 30),
]
dictionary = {}
print(convert(tups, dictionary))
