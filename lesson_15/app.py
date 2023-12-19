from lesson_15.person import Person
from lesson_15.property import Car, House


def life_cicle():
    person = Person()
    while person.bank_account.balance < 140:
        person.work()
    car = Car()
    person.buy_car(car)
    person.work()
    house = House()
    person.buy_house(house)


life_cicle()
