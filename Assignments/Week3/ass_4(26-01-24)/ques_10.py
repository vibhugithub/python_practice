"""
    Q10. Ask 10 numbers from the user and put them into the list. Now remove
    all the even numbers from that list.

"""


user_inputs = []
for _ in range(20):
    try:
        num = int(input("Enter an integer: "))
        user_inputs.append(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")
print("Original list:", user_inputs)
user_inputs = [x for x in user_inputs if x % 2 != 0]

print("Updated list:", user_inputs)
