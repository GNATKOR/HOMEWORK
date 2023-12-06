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
    def __init__(self):
        self.status = "Car is not launched!"

    def launch(self):
        print('Starting the engine')
        self.status = "Started!"

    def move(self):
        if self.status == "Started!":
            print("Ride")
        else:
            print("Cannot ride, launch first")




