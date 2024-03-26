class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of Rs{amount} successful.")
        else:
            print("Invalid Deposit")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of Rs{amount} successful.")
        else:
            print("Invalid Withdrawal amount")

    def bankfees(self):
        fees = 0.05 * self.balance
        self.balance -= fees
        print(f"Bank fees of Rs{fees} applied")

    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")


account1 = BankAccount(accountNumber=123456, name="Varshitha", balance=1000)

account1.display()
account1.deposit(1000)
account1.withdraw(500)
account1.bankfees()

account1.display()
