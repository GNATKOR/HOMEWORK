class Property:
    def __init__(self, value):
        self.value = value


class Car(Property):
    def __init__(self):
        super().__init__(40)


class House(Property):
    def __init__(self):
        super().__init__(100)
