from abc import ABC, abstractmethod

class ATM(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass


class SBIATM(ATM):

    def withdraw(self, amount):
        print(f"₹{amount} withdrawn successfully")


atm = SBIATM()
atm.withdraw(500)