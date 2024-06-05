from account import Account


class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)


currentAccount = CurrentAccount()
currentAccount.deposit(0)
currentAccount.withdraw(0)
