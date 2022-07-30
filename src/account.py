"""
Classrom work
"""

class Account:
    interest = 0.2
    def __init__(self, account_holder):
        self.balance = 100000
        self.holder = account_holder

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return ("Insufficient funds")
        self.balance -= amount
        return self.balance

my_account = Account("Tatiana")
other_account = Account("Random Person")
