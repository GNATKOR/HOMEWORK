from lesson_12.type import Animal, Transport


class Duck(Animal):
    def voice(self):
        print('quack, quack')

    def move(self):
        print('swims')


class Tiger(Animal):
    def voice(self):
        print('roar!')

    def move(self):
        print('running')


class Car(Transport):
    def move(self):
        print("Ride")

    def launch(self):
        print('Starting the engine')
