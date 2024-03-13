"""
    Q9. Take values of length and breadth of a rectangle from user and check if
    it is square or not.
"""

length_input = int(input("Enter the length of rectangle: "))
breadth_input = int(input("Enter the breath of rectangle: "))

if length_input == breadth_input:
    print("IT's square....")
else:
    print("NOT Square")
