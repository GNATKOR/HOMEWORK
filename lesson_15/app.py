from random import randint


class Person:
    def __init__(self):
        self._bank_account = 0
        self.movable = None
        self.realty = None

    @property
    def bank_account(self):
        return self._bank_account

    def work(self):
        income = randint(5, 10)
        self._bank_account += income
        print(f'You have earned {income} coins!')

    def buy_car(self):
        if self._bank_account >= 40:
            self._bank_account -= 40
            self.movable = 'Car'
            print('You have successfully BOUGHT the CAR!')
        else:
            print('Insufficient funds.')

    def buy_house(self):
        if not self.movable:
            print('You should buy a car first!')
        elif self._bank_account <= 100:
            print('Insufficient funds.')
        else:
            self.realty = 'House'
            self._bank_account -= 100
            print('You have successfully BOUGHT the HOUSE!')

    def sell_car(self):
        self.movable = None
        self._bank_account += 40
        print('You have successfully SOLD the HOUSE!')

    def sell_house(self):
        self.realty = None
        self._bank_account += 100
        print('You have successfully SOLD the HOUSE!')
