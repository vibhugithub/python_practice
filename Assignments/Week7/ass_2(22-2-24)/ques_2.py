"""

Your class should be named Bank and should contain the following
attributes:
Methods to Implement:
account_holder_name (str): Name of the account holder.
account_number (int): Account number of the account holder.
balance (float): Current balance in the account.
account_type (str): Type of account ('Savings', 'Checking', etc.).

displayAllInfo(): This method should print all information about the
bank account, including the account holder's name, account number,
balance, and account type.
deposit(amount): This method should add the specified amount to the
account balance.
withdraw(amount): This method should deduct the specified amount
from the account balance if sufficient funds are available.
getBalance(): This method should return the current balance in the
account.
Keep in mind you just need to ask account_holder_name and
account_type from the user in __init__() method. The account_number
should be randomly generated between 100000 to 999999 and
balance should automatically set to 100.
Implement the Bank class according to the provided specifications.
Test your class by creating instances of Bank and calling various
methods on them to ensure they work correctly.
Use meaningful variable names and include comments where
necessary to enhance code readability.
"""

import random


class bank:
    def __init__(self) -> None:
        self.holder_name = input("Enter Name of account holder: ")
        self.account_number = int(random.randint(100000, 999999))
        self.balance = float(input("Enter current balance in the account: "))
        self.account_type = input("Type of account ('Savings', 'Checking', etc.): ")

    def displayAllInfo(self):
        print("Bank Information:")
        print(f"Name: {self.holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        print(f"Account Type: {self.account_type}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful.")
        print(f"New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful.")
            print(f"New Balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def getBalance(self):
        return self.balance


if __name__ == "__main__":
    bank_account = bank()

    bank_account.displayAllInfo()

    bank_account.deposit(50.0)
    bank_account.withdraw(30.0)

    print(f"Current Balance: {bank_account.getBalance()}")
