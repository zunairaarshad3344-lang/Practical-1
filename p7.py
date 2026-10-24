class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.balance:
            raise InsufficientFundsError("Insufficient balance")

        self.balance -= amount

    def __str__(self):
        return f"Balance: {self.balance}"


account = BankAccount(1000)

account.deposit(500)
print(account)

account.withdraw(200)
print(account)

try:
    account.withdraw(2000)
except InsufficientFundsError as e:
    print(e)