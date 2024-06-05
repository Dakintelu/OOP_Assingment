from account import Account


class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)
        self.__interest_rate = 0.7 / 100

    def deposit(self, amount):
        rate = self.__interest_rate * amount
        new_amount = amount + rate
        self.balance = new_amount + self.balance
        print('New Balance is:', self.balance)

    def withdraw(self, amount):
        if amount < 700000:
            super().withdraw(amount)
        else:
            print("You cannot withdraw above your limit")


savingsAccount = SavingsAccount()
savingsAccount.withdraw(0)
savingsAccount.deposit(0)
