"""
    Q1. Calculate the cube of all numbers from 1 to a given number
"""


def calculate_cubes(n):
    cubes = []  # List to store the cube of each number
    for num in range(1, n + 1):
        cube = num**3  # Calculate the cube of the current number
        cubes.append(cube)  # Add the cube to the list
    return cubes


# Example usage:
given_number = int(input("Enter a number: "))
cubes = calculate_cubes(given_number)
print("Cubes of numbers from 1 to", given_number, ":", cubes)
