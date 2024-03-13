"""
Q2. Design a class called Product with properties like name, price,
category, and quantity. Implement a constructor to initialize these
attributes.
Add methods to calculate the total price after applying a discount, ask
discount percent within that method.

"""


class Product:
    def __init__(self, name, price, category, quantity):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity

    def apply_discount(self):
        discount_percent = float(input("Enter the discount percentage: "))
        discount_amount = self.price * (discount_percent / 100)
        discounted_price = self.price - discount_amount
        total_price = discounted_price * self.quantity
        return total_price


# Example usage:
product1 = Product("Laptop", 1000, "Electronics", 2)
total_price_after_discount = product1.apply_discount()
print("Total price after discount:", total_price_after_discount)
