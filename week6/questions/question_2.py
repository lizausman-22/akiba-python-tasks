class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder          # public attribute
        self.__balance = initial_balance              # private attribute (name-mangled)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid transaction: Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid transaction: Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Invalid transaction: Insufficient funds.")
            return
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")

    def get_balance(self):
        print(f"Current balance for {self.account_holder}: {self.__balance}")
        return self.__balance

#Encapsulation is the bundling of data (attributes) and the methods that operate on that data into a single unit (a class), while restricting direct access to some of the object’s components
#Private attributes protect the internal state of an object from accidental or unauthorized modification.
#Name mangling is the mechanism Python uses to implement a weak form of “private” attributes. Any identifier that starts with two underscores and does not end with two underscores (e.g. __balance) is automatically renamed by the interpreter to _ClassName__attribute (e.g. _BankAccount__balance).
#Public: Accessible from anywhere
#Protected: Intended for subclasses / internal use only
#Private: Intended to be used only inside the class