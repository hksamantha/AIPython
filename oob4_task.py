class BankAccount:
    def __init__(self):
        self.__balance=0

    def get_balance(self):
        print(self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:

            self.__balance-=amount

New_balance=BankAccount()

New_balance.deposit(50)
New_balance.withdraw(20)
New_balance.get_balance()

