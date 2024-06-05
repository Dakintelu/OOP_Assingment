class Account:
    def __init__(self):
        self.balance = 1000000
        self.__id_number = "FG5TYHD"
        print('Starting balance is: ', self.balance)

    def get_id_number(self):
        return self.__id_number

    def set_id_number(self, new_id_number):
            self.__id_number = new_id_number

    def deposit(self, amount):
        self.balance = (self.balance + amount)
        print('New balance is:', self.balance)

    def withdraw(self, amount):
        self.balance = (self.balance - amount)
        print('New balance is:', self.balance)
