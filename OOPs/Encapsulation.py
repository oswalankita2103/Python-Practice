class BackAccount:
    
    def __init__(self):
        self.__balance = 1000

    def deposit(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance    

ac = BackAccount()
ac.deposit(500)
print(ac.get_balance())