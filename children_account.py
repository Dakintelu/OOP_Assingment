from account import Account

class Children_Account(Account):
    def __init__(self):
        Account.__init__(self)
        self.__interest_rate = 0.7 / 100

    def deposit(self, amount ):
        rate = self.__interest_rate * amount
        new_amount = amount + rate
        self.balance = new_amount + self.balance
        print('New Balance is:', self.balance)

    def withdraw(self, amount):
        print("Cannot withdraw in this account")


amount = int(input("How much do you want to deposit? "))

children_account = Children_Account()
children_account.deposit(amount)
children_account.withdraw(0)
