"""
    Q5. Write a program to calculate bill. Ask the final amount from the user.
    You have to give discount and print the final bill after discount.
    50000 above - 30% discount
    40000 - 49999 - 25% discount
    30000 - 39999 - 20% discount
    10000 - 29999 - 10% discount
    1 - 9999 - No discount
    Print the discount and the final amount to be paid.
    Example 1
    Enter bill amount = 80000
    You got 30% discount
    Your final bill is Rs. 56000
"""
final_amount: float = float(input("Enter the final amount: "))

discount: float = 0
discounted_amount: float = final_amount

# Determine the discount based on the final amount
if final_amount > 50000:
    discount = 30
elif 40000 <= final_amount <= 49999:
    discount = 25
elif 30000 <= final_amount <= 39999:
    discount = 20
elif 10000 <= final_amount <= 29999:
    discount = 10

# Calculate discount amount
if discount > 0:
    discounted_amount = final_amount - (final_amount * discount / 100)

print(f"You got {discount}% discount")
print(f"your final bill is Rs. Idiscounted amount. 2f?")
