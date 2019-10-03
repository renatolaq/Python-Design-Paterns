from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):

        pass

class Bank(Payment):

    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card  # Assume card number is account number
        return self.account


    def __hasFunds(self):
        print("Bank:: Checking if Account", self.__getAccount(), "has enough funds")
        return True


    def setCard(self, card):
        self.card = card


    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
            return False

if __name__ == '__main__':
    bank=Bank()
    card = input("Proxy:: Punch in Card Number: ")
    bank.setCard(card)
    bank.do_pay()
