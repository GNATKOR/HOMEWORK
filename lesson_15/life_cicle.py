from lesson_15.app import Person
Charles = Person()
print(f'You have {Charles.bank_account} coins.')
while Charles.bank_account < 40:
    Charles.work()
Charles.buy_car()
print(f'You have {Charles.bank_account} coins.')
while Charles.bank_account < 100:
    Charles.work()
Charles.buy_house()
print(f'You have {Charles.bank_account} coins.')
print(Charles.movable)
print(Charles.realty)
Charles.sell_car()
Charles.sell_house()
print(f'You have {Charles.bank_account} coins.')
Charles.buy_house()
