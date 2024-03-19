class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def display_balance(self):
        return f"Na účtě máte: {self.balance} Kč."



account = BankAccount("John Doe", 1000)
# Má zvýšit atribut balance o 500
print(account.deposit(500))
# Má snížit atribut balance o 200
print(account.withdraw(200))

print(account.balance)