class Bank:
    def __init__(self):
        self.accountbalance = 0

    def deposit(self, amount):
        self.accountbalance += amount

    def withdraw(self, amount):
        if amount > self.accountbalance:
            return "Error: Insufficient balance"
        else:
            self.accountbalance -= amount

    def viewaccount(self):
        return self.accountbalance