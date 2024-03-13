"""
    Q3. Attempt the same bill calculator question (Week 1 - Assignment 2 -
"""


def bill_amount(final_amount):
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
    print(f"your final bill is Rs. {discounted_amount:.2f}")


final_amount: float = float(input("Enter the final amount: "))

bill_amount(final_amount)
