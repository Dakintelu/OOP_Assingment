from account import Account

class Student_Account(Account):
    def __init__(self):
        Account.__init__(self)

    def deposit(self, amount):
        if amount < 50000:
            super().withdraw(amount)
        else:
            print("You have passed your withdrawal limit")

    def withdraw(self, amount):
        if amount < 2000:
            super().withdraw(amount)
        else:
            print("You have passed your deposit limit")


student_Account = Student_Account()
student_Account.withdraw(200)
student_Account.deposit(50000)