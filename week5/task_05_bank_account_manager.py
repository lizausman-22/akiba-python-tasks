class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount} birr deposited.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money! Withdrawal cancelled.")
        else:
            self.balance = self.balance - amount
            print(f"{amount} birr withdrawn.")

    def display_balance(self):
        print(f"{self.owner}'s balance: {self.balance} birr")

account1 = BankAccount("Abebe", 1000)
account2 = BankAccount("kebede", 2000)

print("=== Account 1 ===")
account1.display_balance()
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(2000)        # This should fail
account1.display_balance()

print("\n=== Account 2 ===")
account2.display_balance()
account2.deposit(1000)
account2.withdraw(500)
account2.display_balance()