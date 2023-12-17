from random import randint
from lesson_15.bank_acc import BankAccount


class Person:
    def __init__(self):
        self.bank_account = BankAccount()
        self.car = None
        self.house = None

    def work(self):
        earnings = randint(5, 10)
        self.bank_account.deposit(earnings)

    def buy_car(self, car):
        if self.bank_account.withdraw(car.value):
            self.car = car
            return True
        return False

    def buy_house(self, house):
        if self.car is not None and self.bank_account.withdraw(house.value):
            self.house = house
            return True
        return False
